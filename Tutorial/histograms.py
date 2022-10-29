import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Histograms basically allow you to visualize the distribution of pixel intensity in any image -> Analyzing
# Histograms -> Graph, Plot and etc.
# What is histogram ? You can consider histogram as a graph or plot, which gives you an overall idea about the intensity distribution of an image. It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and corresponding number of pixels in the image on Y-axis
# BINS is represented by the term histSize in OpenCV docs.
# BINS: The above histogram shows the number of pixels for every pixel value, ie from 0 to 255. ie you need 256 values to show the above histogram. But consider, what if you need not find the number of pixels for all pixel values separately, but number of pixels in a interval of pixel values? say for example, you need to find the number of pixels lying between 0 to 15, then 16 to 31, ..., 240 to 255. You will need only 16 values to represent the histogram. And that is what is shown in example given in OpenCV Tutorials on histograms.
# So what you do is simply split the whole histogram to 16 sub-parts and value of each sub-part is the sum of all pixel count in it. This each sub-part is called "BIN". In first case, number of bins were 256 (one for each pixel) while in second case, it is only 16. BINS is represented by the term histSize in OpenCV docs.
# DIMS: It is the number of parameters for which we collect the data. In this case, we collect data regarding only one thing, intensity value. So here it is 1.
# RANGE: It is the range of intensity values you want to measure. Normally, it is [0, 256], ie all intensity values.

# Plotting Histograms
# There are two ways for this,
#   Short Way: use Matplotlib plotting functions
#   Long Way: use OpenCV drawing functions


img = cv.imread('Photos/person.jpg')
# cv.imshow('Coins', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# masked = cv.bitwise_and(img, img, mask=mask)

# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

# Color Histogram
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    # hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    # hist = np.bincount(img.ravel(), minlength=256) #10X faster
    hist = cv.calcHist([img], [i], None, [256], [0, 256]) # 40X faster
    # plt.plot(hist, color=col)
    plt.hist(hist, 16, [0, 256])
    plt.xlim([0, 256])


# plt.hist(img.flatten(), 16, [0, 256])
plt.show()
# plt.savefig("Photos/histogram.png")


# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img, img, mask=mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv.calcHist([img], [0], None, [16], [0, 256])
hist_mask = cv.calcHist([img], [0], mask, [16], [0, 256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])
plt.show()

# cv.waitKey(0)
