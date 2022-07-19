# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:09:49 2022

@author: enyasdiman
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/enyas/YOLO/sea_beach.jpg")
b, g, r = cv2.split(img)

#img = np.zeros((100,100), np.uint8)#
#cv2.rectangle(img, (0,50), (100,100), (255), -1)
#cv2.circle(img, (50, 50), 25, 127, thickness=-1)

cv2.imshow("img", img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.show()
