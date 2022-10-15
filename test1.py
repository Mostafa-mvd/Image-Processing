import cv2
import numpy as np

#Capture livestream video content from camera 2 (Dummy Camera)
capture = cv2.VideoCapture(2)

while (1):

	# Take each frame
    _, frame = capture.read()

    # Calculation of Canny
    canny = cv2.Canny(frame, 50, 100)

    cv2.imshow('Canny', canny)

    k = cv2.waitKey(5) & 0xFF
    
    if k == 27:
        break
capture.release()
cv2.destroyAllWindows()
capture.release()
