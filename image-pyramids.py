# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:10:04 2022

@author: enyasdiman
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/enyas/YOLO/hand.jpg")

#Gaussian Pyramid
layer= img.copy()
gaussian_pyramid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
    
#cv2.imshow("Gaussian 0", gaussian_pyramid[0])
#cv2.imshow("Gaussian 5", gaussian_pyramid[5])

#Laplacian Pyramid
    #first_layer = cv2.pyrDown(img) #shrink
    #cv2.imshow("first layer", first_layer)
    #expanded_image = cv2.pyrUp(first_layer)
    #cv2.imshow("expanded image", expanded_image) # gonna lose some informations with expanding
    #laplacian = cv2.subtract(img, expanded_image)
    #cv2.imshow("Laplacian", laplacian)

layer = gaussian_pyramid[5]
cv2.imshow("6", layer)
laplacian_pyramid = [layer]
for i in range(5, 0, -1):
    #print(i)
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)
    cv2.imshow(str(i), laplacian)
#image processing

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

