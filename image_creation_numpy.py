import cv2
import numpy as np

image = np.ones((200, 200))

image[:100:][::] = (0,255,0)
cv2.imshow('image', image)
cv2.waitKey(0)