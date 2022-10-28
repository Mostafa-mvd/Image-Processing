# let’s think of an image as a big matrix and a kernel as tiny matrix(at least in respect to the original “big matrix” image)

# We use an odd kernel size to ensure there is a valid integer (x, y)-coordinate at the center of the image

import cv2 as cv


img = cv.imread('Photos/j.png')

rectangle_kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
ellipse_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (9, 9))
cross_kernel = cv.getStructuringElement(cv.MORPH_CROSS, (9, 9))

print(ellipse_kernel)

dilation = cv.dilate(img, cross_kernel, iterations=1)

cv.imshow("Dilation", dilation)

cv.waitKey(0)