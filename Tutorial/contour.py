import cv2 as cv
import numpy as np

# Contours are defined as the line or curve joining all the points along the boundary of an image that are having the same intensity. The contours are a useful tool for shape analysis and object detection and recognition.
# For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
# In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

img = cv.imread("Photos/shapes.png")
blank = np.zeros(img.shape, dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY, cv.BORDER_DEFAULT)
canny = cv.Canny(img, 170, 255)
#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# Contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
# Approximation Method =>‌ Above, we told that contours are the boundaries of a shape with same intensity. It stores the (x,y) coordinates of the boundary of a shape. But does it store all the coordinates ? That is specified by this contour approximation method.
# If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? For eg, you found the contour of a straight line. Do you need all the points on the line to represent that line? No, we need just two end points of that line. This is what cv.CHAIN_APPROX_SIMPLE does. It removes all redundant points and compresses the contour, thereby saving memory.


# What is Hierarchy?
# Normally we use the cv.findContours() function to detect objects in an image, right ? Sometimes objects are in different locations. But in some cases, some shapes are inside other shapes. Just like nested figures. In this case, we call outer one as parent and inner one as child. This way, contours in an image has some relationship to each other. And we can specify how one contour is connected to each other, like, is it child of some other contour, or is it a parent etc. Representation of this relationship is called the Hierarchy.
# mode is related to hierarchy

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# To draw the contours, cv.drawContours function is used. It can also be used to draw any shape provided you have its boundary points. Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours(useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.

# To draw all the contours in an image:
# cv.drawContours(blank, contours, -1, (0, 255, 0), 3)

#‌To draw an individual contour, say 4th contour:
# cv.drawContours(blank, contours, 3, (0, 255, 0), 3)

# But most of the time, below method will be useful:
cnt = contours[5]
cv.drawContours(img, [cnt], 0, (0, 255, 0), 3)


# Contour Features
# To find the different features of contours, like area, perimeter, centroid, bounding box and etc.

# 1) Moments
# Image moments help you to calculate some features like center of mass of the object, area of the object etc.
M = cv.moments(cnt)

# Centroid is given by the below relations:
# The centroid is the term for 2-dimensional shapes. The center of mass is the term for 3-dimensional shapes. For instance, the centroid of a circle and a rectangle is in the middle.
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


# 2) Contour Area = مساحت
# Contour area is given by the below function:
area = cv.contourArea(cnt)
#‌ area = M['m00']


#‌ 3) Contour Perimeter = محیط
# It is also called arc length. It can be found out using cv.arcLength() function. Second argument specify whether shape is a closed contour (if passed True), or just a curve.
perimeter = cv.arcLength(cnt, True)


# 4) Contour Approximation
# you can use these functions to approximate the shape
epsilon = 0.1*cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
# cv.drawContours(img, [approx], 0, 255, 5)


# 5) Convex Hull
# Given a set of points in the plane. the convex hull of the set is the smallest convex polygon that contains all the points of it.
hull = cv.convexHull(cnt)

# 6) Checking Convexity
k = cv.isContourConvex(cnt)

#7)
#Bounding:
# A) Straight Bounding Rectangle
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# B) Rotated Rectangle
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2)

# C) Minimum Enclosing Circle
(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv.circle(img, center, radius, (0, 255, 0), 2)

# D) Fitting an Ellipse
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img, ellipse, (0, 255, 0), 2)

# E) Fitting a Line
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img, (cols-1, righty), (0, lefty), (0, 255, 0), 2)

cv.imshow("Draw Contours", img)

cv.waitKey(0)
