#!/usr/bin/env python3
import numpy as np
import cv2

#template detection i.e.object detection
img=cv2.resize(cv2.imread('assests/soccer_practice.jpg',0),(0,0),fx=0.8,fy=0.8)
template=cv2.imread('assests/ball.PNG',0)
#template=cv2.resize(cv2.imread('assests/shoe.PNG',0),(0,0),fx=0.8,fy=0.8)#for the shoe
h,w=template.shape

#different methods of doing template template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2=img.copy()

    result=cv2.matchTemplate(img2,template,method)#performs convolution

    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
    #returns min,max,location of min,location of max value in the array
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location=max_loc

    bottom_right=(location[0]+w,location[1]+h)
    cv2.rectangle(img2,location,bottom_right,255,5)
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()