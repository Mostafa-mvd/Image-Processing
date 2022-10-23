import cv2 as cv
import sys

# BGR 8-bit format is the default that is used here.
img = cv.imread("Photos/coins.png", cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("coins", img)
# Zero means to wait forever
cv.waitKey(0)