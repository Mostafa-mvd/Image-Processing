import cv2 as cv
import cv2
import numpy as np


img = cv2.imread("Photos/shapes.png")

# Finding Yellow Color
# hue is another name of color
# Pass the BGR values format you want
yellow = np.uint8([[[0, 214, 255]]])
h, s, v = cv.cvtColor(yellow, cv.COLOR_BGR2HSV)[0][0]

# 1:
# Now you take [H-10, 100,100] and [H+10, 255, 255] as the lower bound and upper bound respectively from previous result

# 2:
# you might want to adjust the ranges(+-10, etc):
# lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
# upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])

lower_bound_hue = np.array([h-10, 100, 100])
upper_bound_hue = np.array([h+10, 255, 255])
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, lower_bound_hue, upper_bound_hue)
result = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Result", result)

cv.waitKey(0)
cv2.destroyAllWindows()
