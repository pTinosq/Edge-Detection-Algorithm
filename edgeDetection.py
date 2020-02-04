import PIL
import math
import time
from PIL import Image, ImageEnhance
path = input("Image path: ")
im = Image.open(path)
width, height = im.size
contrast = ImageEnhance.Contrast(im)
#im =contrast.enhance(3)
threshold = int(input("Threshold: "))
rgb_im = im.convert('RGB')

img = Image.new( 'RGB', (width,height), "black") # create a new black image
pixels = img.load() # create the pixel map

def returnEdge(neigh):
    findAVG = []
    num=0
    #red
    for i in neigh:
        if i[0] is not None:
            findAVG.append(i[0])
    for l in findAVG:
        num+=l
    redAVG = int(num/len(findAVG))
    findAVG = []
    num=0
    #green
    for i in neigh:
        if i[1] is not None:
            findAVG.append(i[1])
    for l in findAVG:
        num+=l
    greenAVG = int(num/len(findAVG))
    findAVG = []
    num=0
    #blue
    for i in neigh:
        if i[2] is not None:
            findAVG.append(i[2])
    for l in findAVG:
        num+=l
    blueAVG = int(num/len(findAVG))

    return int(redAVG/1.1), int(greenAVG/1.1), int(blueAVG/1.1)
    
looper = 0
now = time.time()
for i in range(width):
    looper +=1
    if looper == 10:
        looper = 0
        print(f"Row: {i}/{width}")
    for j in range(height):
        r, g, b = rgb_im.getpixel((i, j))
        neighbours=[]
        try:
            upr, upg,upb = rgb_im.getpixel((i, j-1))
            
        except Exception:
            upr, upg,upb = (None,None,None)
        try:
            downr, downg,downb = rgb_im.getpixel((i, j+1))
            
        except Exception:
            downr,downg,downb = (None,None,None)
        try:
            leftr, leftg, leftb = rgb_im.getpixel((i-1, j))
            
        except Exception:
            leftr, leftg, leftb = (None,None,None)
        try:
            rightr, rightg, rightb = rgb_im.getpixel((i+1, j))
            
        except Exception:
            rightr, rightg, rightb = (None,None,None)

        neighbours.append((upr,upg,upb))
        neighbours.append((downr, downg,downb))
        neighbours.append((leftr, leftg, leftb))
        neighbours.append((rightr, rightg, rightb))

        rx,gx,bx = returnEdge(neighbours)

        r #= int(r-rx)
        g = int(g-gx)
        b = int(b-bx)
        if r < 0:
            r=0
        if g < 0:
            g=0
        if b < 0:
            b=0

        if (r+g+b) > threshold:

            r=255
            g=255
            b=255
        else:
            r=0
            g=0
            b=0
            
        pixels[i,j] = (int((r)),int((g)),int((b))) # set the colour accordingly
        
befr = time.time()
print(befr-now)
img.show()
img.save("./edge.jpg")


