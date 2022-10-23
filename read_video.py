import cv2 as cv

# Capture livestream video content from camera 2 (Dummy Camera) or Capture saved videos
capture = cv.VideoCapture("Videos/ball.mp4")

# cap may is initialized
while capture.isOpened():

	# frame -> read from capture frame by frame
    # is_true -> frame is read correctly or not
    is_true, frame = capture.read()

    # cap.read() returns a bool (True/False). If the frame is read correctly, it will be True. So you can check for the end of the video by checking this returned value.
    if not is_true:
        break

    # cv.imshow("Saved Video", frame)
    # wait_number = cv.waitKey(20)  # waitKey -> wait number for key to be pressed if zero it is infinite
    # hex = 0xFF # 255
    # bitwiseAnd_result = wait_number & hex
    # d_key_unicode = ord('d')

    # if d key is pressed
    # if bitwiseAnd_result == d_key_unicode:
    #    break

capture.release()
cv.destroyAllWindows()
