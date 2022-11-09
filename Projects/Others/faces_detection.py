import cv2 as cv

# Face Detection =  Detecting presence of a face
# Face Recognition = Identifying who's face it is
# CascadeClassifier works on grayscale image

face_cascade = cv.CascadeClassifier("Development/haarcascade_face.xml")
face_image = cv.imread("Photos/group.jpg")
gray_image = cv.cvtColor(face_image, cv.COLOR_BGR2GRAY)

# It can detect all the faces
faces = face_cascade.detectMultiScale(gray_image, 1.1, 1)

for (x_begin, y_begin, weight, height) in faces:
    # the tuple above in loop is just coordinates of our faces which founded in an image
    cv.rectangle(face_image, (x_begin, y_begin), (x_begin+weight,
                 y_begin+height), (0, 255, 0), thickness=1)

cv.imshow('Detected Faces', face_image)

cv.waitKey(0)
cv.destroyAllWindows()
