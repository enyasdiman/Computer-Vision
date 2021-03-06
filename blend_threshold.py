# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:57:12 2022

@author: enyasdiman
"""

import cv2
#import numpy as np

img1 = cv2.imread("C:/Users/enyas/YOLO/road-300x169.jpg")
img2 = cv2.imread("C:/Users/enyas/YOLO/car-300x169.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#print(img1[0,0])
#print(img2[0,0])

#weighted = cv2.addWeighted(img1, 1, img2, 0.5, 0) #0.5 transparency
ret, mask = cv2.threshold(img2_gray, 240, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

road = cv2.bitwise_and(img1, img1, mask=mask)
car = cv2.bitwise_and(img2, img2, mask=mask_inv)
result = cv2.add(road, car)


#sum = cv2.add(img1, img2, mask=mask)
cv2.imshow("road backgorund", road)
cv2.imshow("car no backgorund", car)
cv2.imshow("mask", mask)
cv2.imshow("mask inverse", mask_inv)
cv2.imshow("result", result)
#cv2.imshow("sum", sum)
#cv2.imshow("threshold", mask)
#cv2.imshow("img2gray", img2_gray)
#cv2.imshow("weighted", weighted)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()