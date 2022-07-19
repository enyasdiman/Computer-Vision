# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:19:23 2022

@author: enyasdiman
"""

import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
img = cv2.imread("C:/Users/enyas/YOLO/sheet_paper.jpeg")

while True:
    #_, frame = cap.read()
    
    cv2.circle(img, (470, 206), 5, (0, 0, 255), -1)
    cv2.circle(img, (1479, 198), 5, (0, 0, 255), -1)
    cv2.circle(img, (32, 1122), 5, (0, 0, 255), -1)
    cv2.circle(img, (1980, 1125), 5, (0, 0, 255), -1)

    pts1 = np.float32([[470, 206], [1479, 198], [32, 1122], [1980, 1125]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (500, 600))
    
    cv2.imshow("Image", img)
    cv2.imshow("Perspective transformation", result)
    
    #key = cv2.waitKey(1)
    #if key == 27:
     #   break
    
#cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()