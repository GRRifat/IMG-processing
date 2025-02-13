import cv2 as cv 
import numpy as np

img= cv.imread('D:\\Picture of Rifat & video\\im.jpg')
cv.imshow('im', img)

#Translation 
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])  # matrix call float32([----])
    dimensions = (img.shape[1], img.shape[0])  #1 = height 0 = width
    return cv.warpAffine(img, transMat, dimensions)

# - x --- left 
# - y ---- up
#  x --- right
#  y ---- down

translated =translate(img, 100, 100)
cv.imshow('TRANSLATE',translated)

#Rotation 
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
     

     rotPoint = (width//2,height//2)

     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

     dimensions = (width, height)
     return cv.warpAffine(img, rotMat, dimensions)
    
#45 ^0 img 
rotated = rotate(img, -45)
cv.imshow('Rotated',rotated)

#90 ^0 img
rotated_rotated = rotate(img, -90)
cv.imshow('Rotated-Rotated',rotated_rotated)

#Fliping
flip = cv.flip(img,-1)
cv.imshow('FLIP',flip)

#Cropping 
cropped= img[100:200, 200:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
