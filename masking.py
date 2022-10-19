import cv2 as cv
import numpy as np


# size of black and image must be the same
image = cv.imread("Photos/Figure_1.png")
blank = np.zeros((image.shape[:2]), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (image.shape[1]//2 - 50, image.shape[0]//2 - 50), 
(image.shape[1]//2 + 50, image.shape[0]//2 + 50), 255, -1)

circle = cv.circle(blank.copy(), (image.shape[1]//2, image.shape[0]//2), 60 ,255, -1)

weird_shape = cv.bitwise_or(rectangle, circle)

masked = cv.bitwise_and(image, image, mask=weird_shape)

cv.imshow("Mask1", masked)

cv.waitKey(0)
