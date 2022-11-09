import cv2 as cv

shape_image = cv.imread("Photos/shapes.png")

# Grayscale = Binary Image
gray_image = cv.cvtColor(shape_image, cv.COLOR_BGR2GRAY)

# Filtering area you want between 0 (black) and 255 (white)
ret, threshed = cv.threshold(gray_image, 50, 255, 1)

# In this case, contours find information about shapes in our image.
contours, hierarchies = cv.findContours(threshed, 1, 2)

# We have to go into out contours python list
for contour in contours:
    # What are the points that are specifying the contours otherwise, what points say to us? what information they have?
    # approxPolyDP is able to identify number of points (coordinates) you need to define your contours or to draw your shape
    # DP actually the name of person who develop this algorithm (Douglas Peucker)
    # Epsilon value => the amount of error you ok with to identify number of points.
    # arclength function is the distance between two points along a section of a curve.
    # Second argument of arcLength function specify whether shape is a closed contour (if passed True), or just a curve.
    # In our case, all the curve are closed (True)‌ .
    contour_len = cv.arcLength(contour, True)
    epsilon = 0.01 * contour_len # contour_len multiply 0.01 can be more or less acceptable refers to document
    approx = cv.approxPolyDP(contour, epsilon, True)
    approx_len = len(approx) # number of the coordinates = length
    cv.drawContours(shape_image, [contour], 0, 255, 5)

    if approx_len == 4:
        print("This is a square")
    elif approx_len == 6:
        print("This is a hexagon")
    elif approx_len == 3:
        print("This is a triangle")
    elif approx_len > 8:
        print("This is a circle")

cv.imshow("Shapes", shape_image)

cv.waitKey(0)
cv.destroyAllWindows()