import numpy as np
import cv2 as cv

cap = cv.VideoCapture(2)

# Define the codec and create VideoWriter object
# A FourCC ("four-character code") is a sequence of four bytes (typically ASCII) used to uniquely identify data formats.
fourcc = cv.VideoWriter_fourcc(*'MJPG')

out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480), False)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # write the flipped frame
    out.write(gray_frame)
    cv.imshow('frame', gray_frame)
    if cv.waitKey(25) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
