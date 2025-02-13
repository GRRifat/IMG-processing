import cv2 as cv
import numpy as np
img= cv.imread('D:\\Picture of Rifat & video\\lion.jpg')
#cv.imshow('lion', img)

#convrt to gray 
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#Lablacain model
lap = cv.Laplacian(gray, cv.CV_64F)
lab = np.uint8(np.absolute(lap))
cv.imshow('Lap',lap)

#Sobel model
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel= cv.bitwise_or(sobelx, sobely)

cv.imshow('S-X',sobelx)
cv.imshow('S-Y',sobely)
cv.imshow('S-Combined',combined_sobel)

#Canny model Alg
canny= cv.Canny(gray, 150, 150)
cv.imshow('Canny',canny)

cv.waitKey(0)

