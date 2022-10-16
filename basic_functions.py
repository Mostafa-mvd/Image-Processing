import cv2 as cv

main_image = cv.imread("Photos/Figure_1.png") # BGR images
cv.imshow("Main", main_image)


# Converting BGR to grayscale image
# gray_image = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray_image)


# Blur -> Reduce some of noise that exists on image because of camera sensors, bad lighting, etc
# The Gaussian Blur Technique
# ksize -> kernel size -> to compute blown the image -> It has to be odd number
# blur_image = cv.GaussianBlur(main_image, (11, 11), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur_image)


# Edge Cascade
# We can reduce edges by blur_image
# The boundary between black and white is the edge we are looking for, that is, the sharp change between pixels
# canny_image = cv.Canny(main_image, 170, 150)
# cv.imshow("Canny", canny_image)

# Dilating the image : removes noise from the image or settles down any imperfections to make the image very clear
# dilated_image = cv.dilate(canny_image, (11, 11), iterations=1)
# cv.imshow("Dilated", dilated_image)

# Erode the image : the small white noises in the image can be removed, 
# the two connected objects can be detached, etc.
# eroded_image = cv.erode(dilated_image, (3, 3), iterations=2)
# cv.imshow("Eroded", eroded_image)


# Resizing
resized_image = cv.resize(main_image, (400, 400))
cv.imshow("Resized", resized_image)


# Cropping
cropped_image = main_image[300:400, 400:500] # 2D slicing
cv.imshow("Cropped", cropped_image)


cv.waitKey(0)
