# Gradient filters or High-pass filters (Sobel, Scharr and Laplacian) = edges.

# In image processing, when we refer to a "gradient" we usually mean the change in brightness over a series of pixels.
# an example of gradient is a linear gradient from black to white. this particular gradient is smooth, and we wouldn't say there is an "edge" in this image.
# In image processing we can find edges by looking at sharp transitions (sharp gradients) from one brightness to another.
# If we zoom into the upper left corner of gradient.png image, we can see that there is a transition from white to black over just a few pixels. This transition is a gradient, too
# If you want to detect both edges, better option is to keep the output datatype to some higher forms, like cv.CV_16S, cv.CV_64F etc, take its absolute value and then convert back to cv.CV_8U.

import cv2 as cv
import numpy as np

img = cv.imread('Photos/gradient.png')

cv.imshow('Gradient', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_8U)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_8U, 1, 0)
cv.imshow('Sobel X', sobelx)

sobely = cv.Sobel(gray, cv.CV_8U, 0, 1)
cv.imshow('Sobel Y', sobely)

# Combined Sobel
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Scharr()
scharr = cv.Scharr(gray, cv.CV_8U, 0, 1)
cv.imshow('Scharr', scharr)

cv.waitKey(0)
