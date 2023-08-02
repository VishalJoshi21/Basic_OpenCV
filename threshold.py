import cv2

image = cv2.imread('img.jpg')

# Note:- 0- Black & 255- White

# Binary Thresholding
# If pixel >= thresh then maxvalue(white) else 0 (black)
ret, binary = cv2.threshold(src=image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

# Binary-Inv Thresholding
# If pixel >= thresh then  0 (black) else maxvalue(white)
_, binary_inv = cv2.threshold(src=image, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

# Trunc Thresholding
# If pixel >= thresh then threshold else pixel
_, trunc = cv2.threshold(src=image, thresh=50, maxval=255, type=cv2.THRESH_TRUNC)

# TOZERO Thresholding
# If pixel >= thresh then pixel else 0
_, tozero = cv2.threshold(src=image, thresh=127, maxval=255, type=cv2.THRESH_TOZERO)

# TOZERO-Inv Thresholding
# If pixel >= thresh then 0 else pixel
_, tozero_inv = cv2.threshold(src=image, thresh=127, maxval=255, type=cv2.THRESH_TOZERO_INV)

cv2.imshow('Original', image)
cv2.imshow('Binary', binary)
cv2.imshow('Binary INV', binary_inv)
cv2.imshow('Trunc', trunc)
cv2.imshow('TOZERO', tozero)
cv2.imshow('TOZERO INV', tozero_inv)
cv2.waitKey(0)