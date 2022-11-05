import cv2 as cv


def read_image(image_path):
    return cv.imread(image_path)


def show_image(img, delay_ms=0):
    cv.imshow("Image", img)
    cv.waitKey(delay_ms)
    cv.destroyAllWindows()


def clear_image(img):
    resized_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    bilateral = cv.bilateralFilter(resized_gray, 13, 75, 75)
    edged = cv.Canny(bilateral, 30, 200)

    return edged


def get_contours(cleared_img):
    contours, _ = cv.findContours(
        cleared_img.copy(), 
        cv.RETR_LIST, 
        cv.CHAIN_APPROX_SIMPLE)

    sorted_contours = sorted(
        contours, 
        key=cv.contourArea, 
        reverse=True)[:10]

    return sorted_contours


def find_approximate_contours(contours):
    for contour in contours:
        peri = cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) == 4:
            return approx

    return None


def roi(approx_cnt, resized_img):
    x, y, w, h = cv.boundingRect(approx_cnt)

    return resized_img[y:y+h, x:x+w]
