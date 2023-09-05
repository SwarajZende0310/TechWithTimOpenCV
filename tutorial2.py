#!/usr/bin/env python3
import cv2
import random
img =cv2.imread('panda.jpeg',-1)

#print(img)
#print(type(img))
print(img.shape)
#print(img[25][45:100])  printing 25th row and 45 to 100 columns

#Randomly setting pixel values of 1st 50 rows
#for i in range(0,50):
#    for j in range(img.shape[1]):
#       img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

#Copying and pasting a part of the image
tag=img[25:75,50:100]
img[0:50,100:150]=tag
 
cv2.imshow('IMage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()