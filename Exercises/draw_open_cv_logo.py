import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), dtype=np.uint8)

divided_width = img.shape[1]//2
divided_height = img.shape[0]//2
thickness = -1
black_color = (0, 0, 0)
radius = 50
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = cv.LINE_AA
red_color = (0, 0, 255)
green_color = (0, 255, 0)
blue_color = (255, 0, 0)

center_A = (divided_width, divided_height - 100)
center_B = (divided_width - 100, divided_height + 50)
center_C = (divided_width + 100, divided_height + 50)

triangle_points_A = np.array([[center_A[0], center_A[1]],
                            [divided_width - 35, divided_height - 50], 
                            [divided_width + 35, divided_height - 50]], 
                            np.int32)

triangle_points_B = np.array([[center_B[0], center_B[1]],
                            [divided_width - 35, divided_height - 50],
                            [divided_width + 50, divided_height + 50]],
                           np.int32)

triangle_points_C = np.array([[center_C[0], center_C[1]],
                            [divided_width + 35, divided_height - 50],
                            [divided_width + 130, divided_height - 50]],
                           np.int32)

centers = [center_A, center_B, center_C]
colors = [red_color, green_color, blue_color]
triangle_pts = [triangle_points_A, triangle_points_B, triangle_points_C]

for center, color, triangle_points in zip(centers, colors, triangle_pts):
    cv.circle(img, center, radius, color, thickness)
    cv.circle(img, center, radius - 25, black_color, thickness)
    cv.fillPoly(img, pts=[triangle_points], color=black_color)

cv.putText(img, 'OpenCV', (80, 450), font, 3, (255, 255, 255), 2, font_scale)

cv.imshow("OpenCV Logo", img)
cv.waitKey(0)
