# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:02:40 2022

@author: enyasdiman
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/enyas/YOLO/squares.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)
#print(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()