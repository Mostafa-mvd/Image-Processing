import cv2 as cv
import numpy as np

# point =! shape
# point -> (width, height)
# A scalar value refers to a single value

# Draw Blank Image
# The blank_image dimension will have 500 arrays (rows) that contains 500 arrays (columns), each with 3 elements
# this is 3 dimension matrix (3D) -> bcz of len(shape) = len((500, 500, 3)) = 3
# dtype -> 'uint8', np.int8
# initial color will be set to Black
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

# Draw Ellipse
# Axes => Axes often means the "x" and "y" lines that cross at right angles to make a graph.
# cv.ellipse(blank_image, (180, 110), (100, 100), 22, 0, 180, 255, -1)
# cv.imshow("Ellipse", blank_image)

# Draw Polygon
# vertices = vertex = corners
# # Polygon corner points coordinates
penta_points = np.array([[[50, 150], [130, 100], [190, 150], [170, 270], [90, 250]]], np.int32)
# -1 means 'whatever it takes' to flatten
# pts dimension will have whatever it takes for rows that contains one array (column), each with 2 elements
pts = penta_points.reshape(-1, 1, 2)
cv.polylines(blank_image, [pts], False, (0, 255, 255))
# cv.fillPoly(blank_image, pts=[penta_points], color=(255, 0, 0))
cv.imshow("Polygon", blank_image)


# Write Text On Image
# cv.putText(blank_image, "Hello World", (130, 130), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), thickness=3)
#‌ cv.imshow("Text", blank_image)

cv.waitKey(0)
