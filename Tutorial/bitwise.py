import cv2 as cv
import numpy as np

# BGR colors work with 3D matrix
# This includes the bitwise AND, OR, NOT, and XOR operations. They will be highly useful while extracting any part of the image, defining and working with non-rectangular ROI's, and etc.
# Bitwise operations are used in image manipulation and used for extracting essential parts in the image.


# black -> 0
# white -> 1
# base on truth table of logical operations
blank = np.zeros((400, 400, 3), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30, 30), (360, 360), (255, 255, 255), -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (255, 255, 255), -1)
bitwize_and = cv.bitwise_and(rectangle, circle)
bitwize_or = cv.bitwise_or(rectangle, circle)
bitwize_xor = cv.bitwise_xor(rectangle, circle)
bitwize_not = cv.bitwise_not(circle)


cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)
cv.imshow("Bitwise And", bitwize_and)
cv.imshow("Bitwise Or", bitwize_or)
cv.imshow("Bitwise XOR", bitwize_xor)
cv.imshow("Bitwise NOT", bitwize_not)

cv.waitKey(0)

