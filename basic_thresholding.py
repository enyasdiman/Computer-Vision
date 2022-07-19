# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:17:38 2022

@author: enyasdiman
"""

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread("C:/Users/enyas/YOLO/red_panda.jpg", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("Image")
cv2.createTrackbar("Threshold value", "Image", 128, 255, nothing)
while True:
    #print(img.shape)
    
    #print(img[0,0])
    #print(img[0,250])
    #print(img[0,499])
    value_threshold = cv2.getTrackbarPos("Threshold value", "Image")
    _, threshold_binary = cv2.threshold(img, value_threshold, cv2.THRESH_BINARY)
    _, threshold_binary_inv = cv2.threshold(img, value_threshold, cv2.THRESH_BINARY_INV)
    _, threshold_trunc = cv2.threshold(img, value_threshold, cv2.THRESH_TRUNC)
    _, threshold_to_zero = cv2.threshold(img, value_threshold, cv2.THRESH_TOZERO)
    _, threshold_to_zero_inv = cv2.threshold(img, value_threshold, cv2.THRESH_TOZERO_INV)





    cv2.imshow("Image", img)
    cv2.imshow("th binary", threshold_binary)
    cv2.imshow("th binary inv", threshold_binary_inv)
    cv2.imshow("th trunc", threshold_trunc)
    cv2.imshow("th to zero", threshold_to_zero)
    cv2.imshow("th to zero inv", threshold_to_zero_inv)


    key = cv2.waitKey(100)
    if key == 27:
        break
cv2.destroyAllWindows()