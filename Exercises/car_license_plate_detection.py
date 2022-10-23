from cv2 import imshow
import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt

img = cv2.imread('Photos/Plate_Licenses/plate_license_A.jpg')
#convert my image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#perform adaptive threshold so that I can extract proper contours from the image
#need this to extract the name plate from the image.
thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
contours, h = cv2.findContours(thresh, 1, 2)

#once I have the contours list, i need to find the contours which form rectangles.
#the contours can be approximated to minimum polygons, polygons of size 4 are probably rectangles
largest_rectangle = [0, 0]
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:  # polygons with 4 points is what I need.
        area = cv2.contourArea(cnt)
        if area > largest_rectangle[0]:
            #find the polygon which has the largest size.
            largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

x, y, w, h = cv2.boundingRect(largest_rectangle[1])

#crop the rectangle to get the number plate.
# ROI is again obtained using Numpy indexing. Here I am selecting the ball and copying it to another region in the image:
roi = img[y:y+h, x:x+w]

gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
text = pytesseract.image_to_string(roi)
print("License Plate: ", text)
cv2.drawContours(img, [largest_rectangle[1]], 0, (0, 0, 255), -1)
cv2.imshow("roi", roi)
cv2.waitKey(0)
