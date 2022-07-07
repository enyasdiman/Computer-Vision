# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 09:23:08 2022

@author: enyasdiman
"""

import cv2
import numpy as np

image = cv2.imread("C:/Users/enyas/YOLO/flag.png")
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #turning gray


image_grayscale[175, 100] = 255 #255-white

print(image_grayscale)



#print(image[175,300]) #pixel on the center is green, we picked it up
#image[175,300]=(255,0,0) #replace with blue pixel

cv2.imshow("Flag", image_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

#[255   0   0] blue
#[0   255   0] green
#[  0   0 255] red