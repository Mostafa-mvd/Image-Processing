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
import numpy as np


def auto_thresholding(image, sigma=0.33):
	v = np.median(image)
	
	# 1
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	
	# 2
	# lower = 0.66 * v
	# upper = 1.33 * v
	
	return lower, upper

img = cv.imread('Photos/messi.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold1, threshold2 = auto_thresholding(gray)
edges = cv.Canny(img,  threshold1, threshold2)

cv.imshow("Edge", edges)


cv.waitKey(0)