# Python edge detection algorithm

As part of the A-Level OCR B course we have to learn the main different types of image manipulation and how they're achieved.
I decided that the best way for me to learn the algorithm was to make it myself so here is a simple algorithm that'll detect edges and outline them with a white line.

# Dependancy
- Python 3.7+
- [PIL (pillow) module](https://pillow.readthedocs.io/en/stable/)

# How it works
- The user enters a threshold (e.g 55)
- The algorithm loops through every single pixel and gets the RGB values from said pixel. It will then get the mean of the neighbouring pixels and subtract that from the pixel it just read.
- The threshold mentioned above basically states that if the red + green + blue pixel values are larger than or equal to 55, it should make that pixel white, otherwise it should be made black.

# Usage
Run the .py and provide a path to the image <string>. The algorithm works by reading every single pixel in the image therefore I do not recommend using this algorithm on images with a large dimension.
Example path: ../images/baguette.jpg

Then the algorithm will ask you for your threshold `integer`.

The algorithm will proceed to go line by line, row by row and run the algorithm mentioned in the **How it works** section.

Once completed it will show the final image and then it will save it in the same directory as the .py file under the name __edge.jpg__
