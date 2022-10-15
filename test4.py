import cv2

# path
path_1 = r'Figure_3.png'
path_2 = r'Figure_4.png'
image1 = cv2.imread(path_1)
image2 = cv2.imread(path_2)
sum_image = cv2.add(image1, image2)
cv2.imshow('Weighted Image', sum_image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
