# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:29:49 2022

@author: enyasdiman
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/enyas/YOLO/balls.jpg", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(mask, kernel)
erosion = cv2.erode(mask, kernel, iterations=3)

cv2.imshow("Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Dilation", dilation)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

