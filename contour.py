import cv2 as cv
import numpy as np

# Edge detection and contours are used to locate points in images where the color or brightness have great changes.

# Edges could therefore correspond to:
#   Boundaries of an object in an image
#   Boundaries of shadowing or lighting conditions in an image
#   Boundaries of “parts” within an object


img = cv.imread("Photos/Figure_1.png")
blank = np.zeros(img.shape, dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY, cv.BORDER_DEFAULT)

# blur = cv.blur(gray, (3,3))
canny = cv.Canny(img, 170, 255)

# Converting Image to black and white -> Binarizing an image
# below 125 is zero BGR code (black), above 125 is 255 BGR code (white)
# 125 is BGR code of gray color
# 255 is maximum BGR code value and It is white
# threshold in this place means changes of intensity (between white and black)
#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)


# It is like find the edges of an image
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Draw Contours", blank)

cv.waitKey(0)
