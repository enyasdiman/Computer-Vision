# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:10:11 2022

@author: enyasdiman
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 20)
    
    if corners is not None:
        corners = np.int0(corners)
        
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(frame, (x,y), 3, (0,0,255), -1)
    
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()