import cv2 as cv
import numpy as np


main_image = cv.imread("Photos/Figure_1.png")
cv.imshow("Main", main_image)


# OpenCV provides two transformation functions, cv.warpAffine and cv.warpPerspective, with which you can perform all kinds of transformations

# Transformations like rotation, translation, Affine, Perspective

# Translation is the shifting of an object's location

def translate(img, x, y):
    """ shifting the location of the image in the (x,y) direction
        -x --> Left
        -y --> Up
        +x --> Right
        +y --> Down """

    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0]) # (width, height)
    return cv.warpAffine(img, trans_mat, dimensions)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2) #Center of image

    rot_mat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    # relocated the image
    return cv.warpAffine(img, rot_mat, dimensions)


rotated = rotate(main_image, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(main_image, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

translated = translate(main_image, -100, -100)
cv.imshow('Translated', translated)


# Resizing
resized = cv.resize(main_image, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Flipping
# 0 -> Vertically
# 1 -> Horizontally
# -1 -> Both vertically and Horizontally
flipped = cv.flip(main_image, 1)
cv.imshow('Flipped', flipped)


# Cropping
cropped = main_image[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
