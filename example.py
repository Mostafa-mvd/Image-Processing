import cv2
import numpy as np

#Capture livestream video content from camera 2 (Dummy Camera)
capture = cv2.VideoCapture(2)

while (1):

	# Take each frame
    _, frame = capture.read()

	# Convert to HSV for simpler calculations
	# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Calculation of Sobelx
	# sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)

	# Calculation of Sobely
	# sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

	# Calculation of Laplacian
	# laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    # Calculation of Canny
    canny = cv2.Canny(frame, 50, 100)

	# cv2.imshow('Sobelx', sobelx)
	# cv2.imshow('Sobely', sobely)
	# cv2.imshow('Laplacian', laplacian)
    cv2.imshow('Canny', canny)

    k = cv2.waitKey(5) & 0xFF
    
    if k == 27:
        break

cv2.destroyAllWindows()

#release the frame
capture.release()
