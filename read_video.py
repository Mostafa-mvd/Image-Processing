import cv2 as cv

# Capture livestream video content from camera 2 (Dummy Camera) or Capture saved videos
# To capture a video, you need to create a VideoCapture object. Its argument can be either the device index or the name of a video file. A device index is just the number to specify which camera. Normally one camera will be connected (as in my case). So I simply pass 0 (or -1). You can select the second camera by passing 1 and so on. After that, you can capture frame-by-frame. But at the end, don't forget to release the capture. 

capture = cv.VideoCapture("Videos/ball.mp4")

# Sometimes, cap may not have initialized the capture. In that case, this code shows an error. You can check whether it is initialized or not by the method cap.isOpened(). If it is True, OK. Otherwise open it using cap.open().
# capture.open("Videos/ball.mp4")

# You can check whether it is initialized or not by the method cap.isOpened().
if not capture.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    #‌# Capture frame-by-frame
	# frame -> read from capture frame by frame
    # is_true -> frame is read correctly or not, So you can check for the end of the video by checking this returned value.
    is_true, frame = capture.read()

    # cap.read() returns a bool (True/False). If the frame is read correctly, it will be True. So you can check for the end of the video by checking this returned value.
    if not is_true:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)

    # wait 0.025 seconds and go up again
    # 25 milliseconds will be OK in normal cases for playing videos from file.
    key = cv.waitKey(25)
    hex = 0xFF # 255
    bitwiseAnd_result = key & hex
    q_key_unicode = ord('q')

    # if q key is pressed
    if bitwiseAnd_result == q_key_unicode:
        break


# You can also access some of the features of this video using cap.get(propId) method where propId is a number from 0 to 18. Each number denotes a property of the video (if it is applicable to that video)
# Some of these values can be modified using cap.set(propId, value).
width, height = capture.get(cv.CAP_PROP_FRAME_WIDTH), capture.get(cv.CAP_PROP_FRAME_HEIGHT)
print(width, height)

capture.release()
cv.destroyAllWindows()
