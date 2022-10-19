import cv2 as cv
import numpy as np

# RGB colors work with 3D matrix

blank = np.zeros((400, 400, 3), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30, 30), (360, 360), (255, 255, 255), -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (255, 255, 255), -1)
bitwize_and = cv.bitwise_and(rectangle, circle) #intersecting region
bitwize_or = cv.bitwise_or(rectangle, circle) #union region
bitwize_xor = cv.bitwise_xor(rectangle, circle) #non-intersecting region
bitwize_not = cv.bitwise_not(circle) #invert color


cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)
cv.imshow("Bitwise And", bitwize_and)
cv.imshow("Bitwise Or", bitwize_or)
cv.imshow("Bitwise XOR", bitwize_xor)
cv.imshow("Bitwise NOT", bitwize_not)

cv.waitKey(0)

