import cv2 as cv
import numpy as np


#‌ Colors are merged differently by three main channels Green, Red and Blue
# Looking for highly changes (white) in intensity of an image


img = cv.imread("Photos/Figure_1.png")

blank = np.zeros(img.shape[:2], dtype="uint8") # One Dimension

#Splitting
red, green, blue = cv.split(img)


#Merging
merged_channel = cv.merge([red, green, blue]) # [Red, Green, Blue]


#Showing Actual Color of One dimension Image
blue_img = cv.merge([blank, blank, blue])
green_img = cv.merge([blank, green, blank])
red_img = cv.merge([red, blank, blank])


cv.imshow("Main", img)
cv.imshow("Red Channel", red)
cv.imshow("Green Channel", green)
cv.imshow("Blue channel", blue)
cv.imshow("Merged Channel", merged_channel)
cv.imshow("Green Image", green_img)
cv.imshow("Red Image", red_img)
cv.imshow("Blue Image", blue_img)


cv.waitKey(0)
