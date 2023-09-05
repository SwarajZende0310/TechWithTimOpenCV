#!/usr/bin/env python3
import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #changing image from one form to another

    #EXTRACTING Blue colour from Blue
    lower_blue=np.array([90,50,50])#defining lower limit for blue value
    upper_blue=np.array([130,255,255])#defining uppper limit for blue value
    
    #Only keeping particular colour i.e.BLUE and masking all the other pixels
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    
    #Anding the two images and keeping only unmasked pixels 
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',result)
    #cv2.imshow('mask',mask)

    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


#ACRONYM:
#1.RGB::RED GREEN BLUE
#2.BGR::BLUE GREEN RED
#3.HSV::Hue Saturation and Light/Brightness