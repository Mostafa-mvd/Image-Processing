import matplotlib.pyplot as plt
import cv2 as cv


# Color Spaces = 3 Dimensions = 3 Color Layers

# Color spaces are mathematical models describing the different ways of colors can be represented on digital files and reproduce on different devices.

# Color space is important because it dictates how we see images.

# Color Space = How to color are suppose to be interpreted?

# RGB is a common color spaces for today computer or tv monitors.

# There are different color spaces because of different range of color frequency and that depends on your eye cone cells or your device It can see that range of color or not.

# A color space is an arbitrary agreed upon way to define color. There is any number of ways to visualize color. Each has its different advantages and disadvantages.

# Our eyes perceive color by using color receptors called cones. There are three types of cones in the human eye. Each receives short, medium or long wavelengths, which correspond to blue, green and red, respectively (the primary colors of light).

# Different creative pursuits use color differently and, therefore, utilize different color spaces


# Check color_detection.py exercises.


img = cv.imread("Photos/Figure_1.png")
cv.waitKey(0)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)