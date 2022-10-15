import cv2

# path
path = r'Figure_1.png'

# Using cv2.imread() method
# Using 0 to read image in grayscale mode
image = cv2.imread(path, 0)

# Displaying the image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Extracting the height and width of an image -> shape is a tuple
# h, w = image.shape[:2]
# Displaying the height and width
# print("Height = {},  Width = {}".format(h, w))
# print(image.shape)


# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
# (B, G, R) = image[100, 100]

# Displaying the pixel values
# print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel
# B = image[100, 100, 0]
# print("B = {}".format(B))
