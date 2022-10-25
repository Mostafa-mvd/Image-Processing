import cv2 as cv
import sys

# BGR 8-bit format is the default that is used in openCV.
# IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.
img = cv.imread("Photos/coins.png", cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Coins", img)

# Zero means to wait forever
# Measured in milliseconds
# millisecond = 1/1000 seconds
# 3 seconds = 3 * 1000 milliseconds
# 3 milliseconds = 3 * 10^-3 = 0.003 mil
key = cv.waitKey(5000)

if key == ord("s"):
    cv.imwrite("Photos/coins.jpg", img)
