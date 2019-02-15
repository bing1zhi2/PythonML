# -*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt


###
### 测试文字图片锐化的方法，
k=1

img = cv2.imread('text.jpg')


# blur = cv2.blur(img,(5,5))
blur = cv2.GaussianBlur(img,(3,3),3)

mask = cv2.subtract(img,blur)
result_img = cv2.addWeighted(img,1.0,mask,k,0)

mask_abs = cv2.absdiff(img,blur)
result_abs = cv2.addWeighted(img,1.0,mask,k,0)


img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur2 = cv2.GaussianBlur(img2,(5,5),3)
mask2 = cv2.subtract(img2,blur2)
result_img2 = cv2.addWeighted(img2,1.0,blur2,k,0)

b_show=cv2.cvtColor(result_img2,cv2.COLOR_GRAY2BGR)


b, g, r = cv2.split(img)
img2_rgb = cv2.merge([r, g, b])

# b_show=cv2.cvtColor(mmm,cv2.COLOR_GRAY2BGR)

b, g, r = cv2.split(result_img)
blur_rgb = cv2.merge([r, g, b])

b, g, r = cv2.split(b_show)
blur_rgb2 = cv2.merge([r, g, b])

b, g, r = cv2.split(result_abs)
b_abs = cv2.merge([r, g, b])


plt.subplot(131),plt.imshow(img2_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur_rgb),plt.title('Blurred')
plt.subplot(133),plt.imshow(b_abs),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


# # test for a gray image
# img1 = cv2.imread("text.jpg")
# # using opencv
# cv2.imshow("Gray(opencv)", img1)
# # using matplotlib
# plt.imshow(img1)
# plt.show()

# # test for a color image
# img2 = cv2.imread("text.jpg")
# b, g, r = cv2.split(img2)
# img2_c = cv2.merge([r, g, b])
# # using opencv
# cv2.imshow("Color(opencv, img2)", img2)
# cv2.imshow("Color(opencv, img2_c)", img2_c)
# # using matplotlib
# plt.subplot(121)
# plt.imshow(img2)
# plt.subplot(122)
# plt.imshow(img2_c)
# plt.show()
