import cv2

image1 = cv2.imread('img1.jpeg')
image2 = cv2.imread('img2.jpeg')
image1 = cv2.resize(image1, (480, 480))
image2 = cv2.resize(image2, (480, 480))

res_add = cv2.add(image1, image2)
res_sub = cv2.subtract(image1, image2)
res_mul = cv2.multiply(image1, image2)
res_div = cv2.divide(image1, image2)

# addWeighted use for blending image.
# Formula:- Image = (alpha * src1) + (beta * src2) + y
res = cv2.addWeighted(src1=image1, alpha=0.8, src2=image2, beta=0.2, gamma=0)
print(res)
cv2.imshow('image', res)
cv2.waitKey(0)
