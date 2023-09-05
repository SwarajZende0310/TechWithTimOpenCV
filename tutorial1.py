#!/usr/bin/env python3
import cv2 

#importing an image in variable
img=cv2.imread('panda.jpeg',-1)

#resizing an image
#img=cv2.resize(img,(800,800))
img=cv2.resize(img,(0,0),fx=4,fy=4)

#rotating an image
img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

#writing on an new image
cv2.imwrite('new_img.jpeg',img)

#displaying an image in window
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


