import cv2 as cv


# Simple Thresholding / Global Thresholding / Binary Thresholding

# The basic Thresholding technique is Binary Thresholding. For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0 (black), otherwise, it is set to a maximum value.
# ‘255’ is the brightest and ‘0’ the darkest. Recall that grayscale intensities range from pure black (0) to pure white (255)
# So, reading numbers in the thresholded image is much easier than reading numbers in the original image. Not surprisingly, even text-recognition algorithms find it easier to process a thresholded image over the original
# When the thresholding rule is applied equally to every pixel in the image, and the threshold value is fixed, the operations are called global.

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)


# Adaptive Thresholding
# It is useful when an image has different lighting conditions in different areas.
# Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.

adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
