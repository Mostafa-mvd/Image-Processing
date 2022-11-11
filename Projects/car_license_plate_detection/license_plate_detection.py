import cv2 as cv


def read_image(image_path):
    return cv.imread(image_path)


def show_image(img, delay_ms=0):
    cv.imshow("Image", img)
    cv.waitKey(delay_ms)
    cv.destroyAllWindows()


def filter_image(img):
    # Binarize Image (Change Color Space)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Blurring (Smoothing)
    bilateral = cv.bilateralFilter(gray_img, 13, 75, 75)
    # Edge Detection
    edged = cv.Canny(bilateral, 30, 200)

    return edged


def get_contours(filtered_image):
    contours, _ = cv.findContours(
        filtered_image.copy(), 
        cv.RETR_LIST, 
        cv.CHAIN_APPROX_SIMPLE)

    sorted_contours = sorted(
        contours, 
        key=cv.contourArea, 
        reverse=True)[:10]

    return sorted_contours


def approximate_contours(contours):
    for contour in contours:
        perimeter = cv.arcLength(contour, True)
        epsilon = 0.02 * perimeter
        approx = cv.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            return approx

    return None


def roi(approx_cnt, img):
    x, y, w, h = cv.boundingRect(approx_cnt)

    return img[y:y+h, x:x+w]
