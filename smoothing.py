# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:50:42 2022

@author: enyasdiman
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/enyas/YOLO/balloons_noisy.png")

averaging = cv2.blur(img, (5,5))
gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 5, 12, 12) #keeps the edges

cv2.imshow("Original image", img)
cv2.imshow("Averaging image", averaging)
cv2.imshow("Gaussian image", gaussian)
cv2.imshow("Median image", median)
cv2.imshow("Bilateral image", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
