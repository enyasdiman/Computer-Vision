# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:02:20 2022

@author: enyasdiman
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/enyas/YOLO/panda.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (5,5), 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0) # 1 and 0 are the axises
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

canny = cv2.Canny(img, 100, 150) #important

cv2.imshow("Image", img)
cv2.imshow("Sobelx", sobelx)
cv2.imshow("Sobely", sobely)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()