# https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
import cv2

img = cv2.imread('img.jpg')
img = cv2.resize(img, dsize=(0, 0), fx=0.9, fy=0.9)
cv2.line(img=img, pt1=(150, 250), pt2=(300, 400), color=(255, 255, 255), thickness=20, lineType=cv2.LINE_AA)
cv2.arrowedLine(img, (300, 500), (400, 600), color=(255, 255, 255), thickness=20, tipLength=0.2)
cv2.imshow('img', img)
cv2.waitKey(0)
