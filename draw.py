import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')

"""
cv.imshow('Blank', blank)
blank[:]= 0,255,0
cv.imshow('Green',blank)

img = cv.imread("D:\\Picture of Rifat & video\\rifat.jpg")
cv.imshow('rifat',img)

#draw rectangle shape
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2)
cv.imshow('Rectangle',blank)

#draw shape rectangle colour 
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

#All draw shape
cv.rectangle(blank,(0,0),(250,500),(0,250,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)
"""

#circle draw 
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,250,0),thickness=2)
cv.imshow('Circle',blank)

#LINE draw 
cv.line(blank,(100,250),(300,400), (2500,255,255),thickness=2)
cv.imshow('Line',blank)

#text type
cv.putText(blank,'hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)

