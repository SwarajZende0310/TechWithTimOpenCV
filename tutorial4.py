#!/usr/bin/env python3
import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    img=cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    #cv2.line(image_to_work_on,starting_pt,ending_pt,colour_in_BGR,thickness_of_line)
    img=cv2.line(img,(0,height),(width,0),(0,0,255),10)

    img=cv2.rectangle(img,(100,100),(400,400),(128,128,128),10)
    #cv2.rectangle(image_to_work_on,left_hand_top_corner,right_hand_bottom_corner,colour,thickness)
    #if thickness=-1 fills the complete rectangle

    img=cv2.circle(img,(300,300),60,(0,255,0),-1)
    #cv2.circle(image_to_work_on,center_position,radius,colour,thickness)

    #creating a font
    font=cv2.FONT_HERSHEY_SIMPLEX

    #INSERING TEXT
    img=cv2.putText(img,'CONFUSED!!!', (10,height-30),font,2,(0,0,0),8,cv2.LINE_AA)
    #cv2.putText(image_to_work_on,bottom_left_corner,font,font_scale,colour,thickness,line_type)
    
    cv2.imshow('frame',img)

    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
