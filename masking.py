import cv2 as cv
import numpy as np


#1

image = cv.imread('Photos/shapes.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(gray, 92, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
masked1 = cv.bitwise_and(image, image, mask=mask_inv)
noiseless_image_bw = cv.fastNlMeansDenoising(masked1, None, 40, 7, 40)
cv.imshow("Mask1", noiseless_image_bw)


#2

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(gray, 92, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
masked1 = cv.bitwise_and(image, image, mask=mask_inv)

gray = cv.cvtColor(masked1, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(gray, 80, 255, cv.THRESH_BINARY)

# erosion followed by dilation.
# MORPH_OPEN = open(src,element) = dilate(erode(src,element))
opening_mask = cv.morphologyEx(mask, cv.MORPH_OPEN, (3, 3))

masked1 = cv.bitwise_and(masked1, masked1, mask=opening_mask)

cv.imshow("Mask2", masked1)


#2

red = np.uint8([[[0, 0, 255]]])
h, s, v = cv.cvtColor(red, cv.COLOR_BGR2HSV)[0][0]
lower_bound_hue = np.array([h-10, 100, 100])
upper_bound_hue = np.array([h+10, 255, 255])
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, lower_bound_hue, upper_bound_hue)
masked2 = cv.bitwise_and(image, image, mask=mask)

cv.imshow("Mask3", masked2)


#3

blank = np.zeros((image.shape[:2]), dtype="uint8")

rectangle = cv.rectangle(blank, (image.shape[1]//2 - 50, image.shape[0]//2 - 50), 
(image.shape[1]//2 + 50, image.shape[0]//2 + 50), 255, -1)

circle = cv.circle(blank, (image.shape[1]//2, image.shape[0]//2), 60 ,255, -1)

weird_shape = cv.bitwise_or(rectangle, circle)

masked3 = cv.bitwise_and(blank, blank, mask=weird_shape)

cv.imshow("Mask4", masked3)

cv.waitKey(0)
