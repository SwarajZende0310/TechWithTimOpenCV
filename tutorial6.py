#!/usr/bin/env python3
import numpy as np
import cv2

#Corner Detection
img=cv2.imread('assests/chessboard.png')
img=cv2.resize(img,(0,0),fx=0.75,fy=0.75)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting to gray scale so that algorithm can work

#Shi tomashi corner detection algorithm
corners=cv2.goodFeaturesToTrack(gray,100,0.01,10)
#cv2.goodFeaturesToTrack(image_to_work_on,number_of_points_it_will_return,quality_of_corners(Range:0-1),Min_euclidean_distance_between_2corners)

#print(corners) //all values are of float type
#converting all the float values to integers
corners=np.int0(corners)

#Drawing Corners
for corner in corners:
    x,y=corner.ravel()#flattens the array in single dimensional array
    cv2.circle(img,(x,y),5,(255,0,0),-1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1=tuple(corners[i][0])
        corner2=tuple(corners[j][0])
        color=tuple(map(lambda x:int(x) ,np.random.randint(0,255,size=3)))  #generating 3 random integer
        cv2.line(img,corner1,corner2,color,1,cv2.LINE_AA)


cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()