import cv2 as cv
import numpy as np

img= cv.imread('D:\\Picture of Rifat & video\\lion.jpg')
cv.imshow('lion', img)

blank= np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

mask = cv.circle(blank,(img.shape[1]//2 -20, img.shape[0]//2 -20),100, 255, -1)
cv.imshow('Mask',mask)

# mask = cv.rectangle(blank,(img.shape[1]//2 +100, img.shape[0]//2 -50),(img.shape[1]//2 +2, img.shape[0]//2 +40) ,255, -1) # top botton left right
# cv.imshow('Mask',mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)  
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

weird_shape= cv.bitwise_and(circle,rectangle)
cv.imshow('Weird shape ',weird_shape)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)

cv.waitKey(0)
