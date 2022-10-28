import cv2 as cv
import numpy as np


img = cv.imread('Photos/j.png')
j_noise_img = cv.imread('Photos/j_noise.png')
j_holes_img = cv.imread('Photos/j_holes.png')

kernel = np.ones((5,5),np.uint8)


# Low-Pass-Filters for reducing noise


erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img, kernel, iterations=1)

# Opening is just another name of erosion followed by dilation.
opening = cv.morphologyEx(j_noise_img, cv.MORPH_OPEN, kernel)

# It is useful in closing small holes inside the foreground objects, or small black points on the object.
closing = cv.morphologyEx(j_holes_img, cv.MORPH_CLOSE, kernel)

# It is the difference between dilation and erosion of an image.
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

# It is the difference between input image and Opening of the image
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)


# It is the difference between the closing of the input image and input image.
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow("j", img)
cv.imshow("Erosion", erosion)
cv.imshow("Dilation", dilation)
cv.imshow("Opening", opening)
cv.imshow("closing", closing)
cv.imshow("Gradient", gradient)
cv.imshow("Top Hat", tophat)
cv.imshow("Black Hat", blackhat)

cv.waitKey(0)