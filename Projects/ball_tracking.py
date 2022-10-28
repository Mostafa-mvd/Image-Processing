import cv2 as cv
import numpy as np


ball = list()

capture = cv.VideoCapture("Videos/ball.mp4")

frame_width = int(capture.get(3)) 
frame_height = int(capture.get(4)) 
size = (frame_width, frame_height)

output_writer = cv.VideoWriter(
    "Videos/ball_line.avi", 
    cv.VideoWriter_fourcc("M", "J", "P", "G"), 
    10, 
    size)


while capture.isOpened():
    is_correct, frame = capture.read()
    if not is_correct:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_bound_hue = np.array([21, 0, 0])
    upper_bound_hue = np.array([45, 255, 255])
    mask = cv.inRange(hsv, lower_bound_hue, upper_bound_hue)
    (contours, _) = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    center = None

    if len(contours) > 0:
        max_contour = max(contours, key=cv.contourArea)
        # Finding Circle Specification
        ((x, y), r) = cv.minEnclosingCircle(max_contour)
        # Finding Where The Center Of Circle Is
        moment = cv.moments(max_contour)
        try:
            center = (int(moment["m10"]/moment["m00"]), int(moment["m01"]/moment["m00"]))
            # Draw based on center
            cv.circle(frame, center, 10, (255, 0, 0), -1)
            ball.append(center)
        except:
            pass

        if len(ball) > 2:
            for i in range(1, len(ball)):
                cv.line(frame, ball[i-1], ball[i], (255, 0, 0), 3)

    output_writer.write(frame)
