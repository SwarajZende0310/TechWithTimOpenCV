#!/usr/bin/env python3
import numpy as np
import cv2

cap=cv2.VideoCapture(0) #put the path to the video file to load in place of integerargument

#Display the video camera feed till 'q' key is pressed
while True:
    ret,frame=cap.read() #cap.read() reads a frame from the device
    #ret:: tells whether the capture has happened correctly

    #mirroring image multiple times
    image=np.zeros(frame.shape,np.uint8)#creating an numpy array with all zeros and the same shape as frame
    #np.uint8::is the type of the numpy array

    #shrinnking the frame by half
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    #but as we are doing half width as well as height frame becomes 4 times smaller

    #getting the width and height of the image to paste the image
    width=int(cap.get(3))#  3:: gives the width property of the captured image
    height=int(cap.get(4))#  4:: gives the height property of the captured image
    
    #copying hte reduced frame into the image
    image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180) #Top left
    image[height//2:,:width//2]=smaller_frame  #Bottom left
    image[:height//2,width//2:]=cv2.rotate(smaller_frame,cv2.ROTATE_180)  #Top right
    image[height//2:,width//2:]=smaller_frame #Bottom right
    
    cv2.imshow('frame',image)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()