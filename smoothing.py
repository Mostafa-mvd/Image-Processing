
# Image Blurring (Image Smoothing)
# Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. It actually removes high frequency content (eg: noise, edges) from the image. So edges are blurred a little bit in this operation (there are also blurring techniques which don't blur the edges). OpenCV provides four main types of blurring techniques.


import cv2 as cv

# Smoothing, also called blurring, is a simple and frequently used image processing operation.
# A window that will be draw over specific portion of an image -> kernel
# Size of a window = kernel size -> number of row and number of columns -> (3, 3)
# Window contains pixels
# The intention of our blurring methods have been to reduce noise and detail in an image; however, as a side effect we have tended to lose edges in the image.

img = cv.imread("Photos/Figure_1.png")


# Averaging Blur
# blur is applied to the middle pixel as a result of the pixel around it, also called surrounding pixels
# Averaging -> Averaging of surrounding pixel intensities for middle pixel of kernel, This allows us to reduce noise and the level of detail, simply by relying on the average
# This kernel is going to slide from left-to-right and from top-to-bottom for each and every pixel in our input image.
#The pixel at the center of the kernel (and hence why we have to use an odd number, otherwise there would not be a true “center”) is then set to be the average of all other pixels surrounding it. for example with 4x4 we don't have true center for averaging
avg = cv.blur(img, (7, 7))
cv.imshow("Blur", avg)


# Gaussian Blur
# It is like averaging method but each running pixel is given particular weight
# It is less blur than averaging method but more natural
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian", gaussian)

# Median Blur
# using median of surrounding pixel intensities instead of averaging for center pixel
# reducing more noise than two previous methods
median = cv.medianBlur(img, 7)
cv.imshow("Median", median)


# Bilateral Blur
# d = diameter = the larger this diameter is, the more pixels will be included in the blurring computation
# sigmaColor = A larger value for means that more colors in the neighborhood will be considered when computing the blur
# sigmaSpace = A larger value of means that pixels farther out from the central pixel diameter will influence the blurring calculation.
# cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters.
# Bilateral filtering also takes a Gaussian filter in space, but one more Gaussian filter which is a function of pixel difference. The Gaussian function of space makes sure that only nearby pixels are considered for blurring, while the Gaussian function of intensity difference makes sure that only those pixels with similar intensities to the central pixel are considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.

bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
