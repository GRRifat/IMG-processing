import cv2 as cv 
import numpy as np 

img= cv.imread('D:\\Picture of Rifat & video\\im.jpg')
cv.imshow('im', img)

blank = np.zeros(img.shape[:2],dtype ='uint8')

b,g,r = cv.split(img)

blue= cv.merge([b,blank,blank])
green= cv.merge([blank,g,blank])
red= cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Gray',green)
cv.imshow('Red',red)


# cv.imshow('Blue',b)
# cv.imshow('Gray',g)
# cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

marge = cv.merge([b,g,r])
cv.imshow('m',marge)

cv.waitKey(0)