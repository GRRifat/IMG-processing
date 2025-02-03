import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)  
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#Bitwase AND
bitwase_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwase',bitwase_and)

#Bitwase OR
bitwase_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwase_OR',bitwase_or)

#bitwase Xor
bitwase_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwase_XOR',bitwase_xor)

#Bitwase not
bitwase_not = cv.bitwise_not(circle)
cv.imshow('Bitwase_NOT',bitwase_not)

cv.waitKey(0)