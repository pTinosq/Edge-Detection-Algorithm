import PIL
import math
import time
from PIL import Image, ImageEnhance

# Get information regarding image location, size, user defined threshold and the image pixel map
path = input("Image path: ")
image = Image.open(path)
width, height = image.size
threshold = int(input("Threshold: "))
rgb_image = image.convert('RGB')
image_new = Image.new('RGB', (width, height), "black")  # create a new black image
pixels = image_new.load()  # create the pixel map


def returnEdge(neighbouringPixels):
    """
    This function takes in the the neighbouring pixels and applies the average of them to the original pixel
    :param neighbouringPixels:
    :return tuple with new RGB values:
    """

    # Red of each pixel
    findAVG = []
    pixelsNumber = 0
    for i in neighbouringPixels:
        # Checks to ensure that the pixel isn't outside of the image bounds
        if i[0] is not None:
            findAVG.append(i[0])
    for l in findAVG:
        pixelsNumber += l
    redAVG = int(pixelsNumber / len(findAVG))

    # Green of each pixel
    findAVG = []
    pixelsNumber = 0
    for i in neighbouringPixels:
        if i[1] is not None:
            findAVG.append(i[1])
    for l in findAVG:
        pixelsNumber += l
    greenAVG = int(pixelsNumber / len(findAVG))

    # Blue of each pixel
    findAVG = []
    pixelsNumber = 0
    for i in neighbouringPixels:
        if i[2] is not None:
            findAVG.append(i[2])
    for l in findAVG:
        pixelsNumber += l
    blueAVG = int(pixelsNumber / len(findAVG))

    return int(redAVG / 1.1), int(greenAVG / 1.1), int(blueAVG / 1.1)


looper = 0
timeNow = time.time()
for i in range(width):
    looper += 1
    if looper == 10:
        looper = 0
        print(f"Row: {i}/{width}")
    for j in range(height):
        r, g, b = rgb_image.getpixel((i, j))
        neighbours = []
        try:
            upr, upg, upb = rgb_image.getpixel((i, j - 1))

        except Exception:
            upr, upg, upb = (None, None, None)
        try:
            downr, downg, downb = rgb_image.getpixel((i, j + 1))

        except Exception:
            downr, downg, downb = (None, None, None)
        try:
            leftr, leftg, leftb = rgb_image.getpixel((i - 1, j))

        except Exception:
            leftr, leftg, leftb = (None, None, None)
        try:
            rightr, rightg, rightb = rgb_image.getpixel((i + 1, j))

        except Exception:
            rightr, rightg, rightb = (None, None, None)

        neighbours.append((upr, upg, upb))
        neighbours.append((downr, downg, downb))
        neighbours.append((leftr, leftg, leftb))
        neighbours.append((rightr, rightg, rightb))

        rx, gx, bx = returnEdge(neighbours)

        r = int(r - rx)
        g = int(g - gx)
        b = int(b - bx)
        if r < 0:
            r = 0

        if g < 0:
            g = 0

        if b < 0:
            b = 0

        if (r + g + b) > threshold:
            r = 255
            g = 255
            b = 255

        else:
            r = 0
            g = 0
            b = 0

        pixels[i, j] = (int((r)), int((g)), int((b)))  # set the colour accordingly

# Shows image, saves it as edge.jpg and shows how long it took to complete.
timeBefore = time.time()
print(timeBefore - timeNow)
image_new.show()
image_new.save("./edge.jpg")
