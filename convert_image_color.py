import cv2

image = cv2.imread('img.jpg', 1)

image = cv2.cvtColor(image, code=cv2.COLOR_BGR2HSV)
print(image)
cv2.imshow('image', image)
cv2.waitKey(0)