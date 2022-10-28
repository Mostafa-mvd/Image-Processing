# Gradients =! Edges
# Edge detection is an image-processing technique, which is used to identify the boundaries (edges) of objects, or regions within an image.
# Edges are characterized by sudden changes in pixel intensity. To detect edges, we need to go looking for such changes in the neighboring pixels.
# We are using gradient in canny edge detection (canny filter).
# Steps:
#   Noise Reduction -> Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter.
#   Finding Intensity Gradient of the Image (finding edge gradient and direction for each pixel) with with a Sobel kernel Size
#   Non-maximum Suppression
#   Hysteresis Thresholding


# Edges could therefore correspond to:
#   Boundaries of an object in an image
#   Boundaries of shadowing or lighting conditions in an image
#   Boundaries of “parts” within an object


import cv2 as cv

img = cv.imread('Photos/messi.png', 0)
edges = cv.Canny(img, 100, 200)
cv.imshow("Edge", edges)
cv.waitKey(0)