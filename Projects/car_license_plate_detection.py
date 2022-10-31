import cv2
from pytesseract import image_to_string

# F, C pics works for roi and find contours
# C pic works for print car license plate

img = cv2.imread('Photos/Plate_Licenses/Cars Wallpaper - 120.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(
    gaussian, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 9)

# thresh_negative = abs(255-thresh)

noiseless_image_gray = cv2.fastNlMeansDenoising(thresh, None, 20, 7, 21)
# dilation = cv2.dilate(noiseless_image_gray, (3, 3), iterations=3)
# erosion = cv2.erode(noiseless_image_gray, (3, 3), iterations=3)
# opening = cv2.morphologyEx(noiseless_image_gray, cv2.MORPH_OPEN, (17, 17))

contours, hierarchies = cv2.findContours(
    noiseless_image_gray, 
    cv2.RETR_LIST, 
    cv2.CHAIN_APPROX_SIMPLE)

largest_rectangle = [0, 0, 0]

for cnt in contours[0: len(contours) - 1]:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        area = cv2.contourArea(cnt)
        if area > largest_rectangle[0]:
            largest_rectangle = [area, cnt, approx]
            cv2.drawContours(img, [largest_rectangle[1]], 0, (0, 0, 255), 1)


cv2.drawContours(img, [largest_rectangle[1]], 0, (0, 0, 255), 5)

x, y, w, h = cv2.boundingRect(largest_rectangle[1])
roi = img[y:y+h, x:x+w]
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(
     gray, 255, 
     cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
     cv2.THRESH_BINARY, 
     11, 2)

car_license_plate_text = image_to_string(gray)

print("Car License Plate: ", car_license_plate_text)

cv2.imshow("roi", roi)
# cv2.imshow("img", img)
# cv2.imshow("noiseless", noiseless_image_gray)
# cv2.imshow("gray", gray)

cv2.waitKey(0)
