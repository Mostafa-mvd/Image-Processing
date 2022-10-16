import cv2 as cv
import numpy as np

# point =! shape
# point -> (width, height)

# Draw Blank Image
# there are 500 matrices of the shape 500x3 (500 rows and 3 columns) with all array elements is zero
# this is 3 dimension matrix (3D) -> bcz of len(shape) = len((500, 500, 3)) = 3
# dtype -> 'uint8', np.int8
blank_image = np.zeros((500, 500, 3), dtype=np.int8)
# cv.imshow("Blank", blank_image)


# Painting image in certain color at specific range of pixel
# blank_image[200:300, 300:400] = 0, 255, 0 # 0, 255, 0 is green color
# cv.imshow("Green", blank_image)


# Draw Rectangle
# thickness -> -1, 3, cv.FILLED
# (0, 0, 255) -> BGR -> Blue Green Red
# (blank_image.shape[0]//2, blank_image.shape[1]//2) = (width, height)
# cv.rectangle(blank_image, (0, 0), (250, 500), (0, 0, 255), thickness=-1)
# cv.rectangle(blank_image, (0, 0), (blank_image.shape[0]//2, blank_image.shape[1]//2), (0, 153, 153), thickness=-1)
# cv.imshow("Green Rectangle", blank_image)


#Draw Circle
# cv.circle(blank_image, (blank_image.shape[0]//2, blank_image.shape[1]//2), 40, (0, 0, 255), thickness=3)
# cv.imshow("Circle", blank_image)


# Draw Line
# cv.line(blank_image, (0, 0), (blank_image.shape[0]//2, blank_image.shape[1]//2), (255, 255, 255), thickness=3)
# cv.imshow("Line", blank_image)


# Write Text On Image
cv.putText(blank_image, "Hello World", (130, 130), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), thickness=3)
cv.imshow("Text", blank_image)

cv.waitKey(0)
