import cv2 as cv
from time import sleep


def changeResolution(cap, width, height):
    # only works on livestream
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(frame, scale=0.75):
    # works for images, videos and livestream
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def close_all_windows(cap):
    cap.release()
    cv.destroyAllWindows()


def resize_image(img):
    resized_image = rescale_frame(img)
    cv.imshow("Resized Image", resized_image)
    cv.waitKey(0)


def resize_video(cap):
    changeResolution(cap, 480*0.75, 640*0.75)

    while True:
        # frame -> read from capture frame by frame
        # is_true -> frame is read correctly or not
        is_success, frame = cap.read()
        # resized_frame = rescale_frame(frame)
        print(frame.shape)

        cv.imshow("Video", frame)
        # cv.imshow("Resized Video", resized_frame)

        # waitKey -> wait number for key to be pressed if zero it is infinite
        wait_number = cv.waitKey(20)
        hex = 0xFF  # 255
        bitwise_and_result = wait_number & hex
        d_key_unicode = ord('d')

        # if d key is pressed
        if bitwise_and_result == d_key_unicode:
            break

# Capture livestream video content from camera 2 (Dummy Camera) or Capture saved videos
capture = cv.VideoCapture(2)
resize_video(capture)

# image = cv.imread("Figure_1.png")
# imshow("Image", image)
# resize_image(image)

close_all_windows(capture)

