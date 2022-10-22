import cv2 as cv
import cv2
import numpy as np


img = cv2.imread("Photos/shapes.png")
# It is BGR format
# Finding Blue Color
# hue is another name of color
lower_bound_blue = np.array([0, 87, 0])
upper_bound_blue = np.array([121, 255, 0])
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, lower_bound_blue, upper_bound_blue)
result = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Result", result)
cv.waitKey(0)
cv2.destroyAllWindows()
