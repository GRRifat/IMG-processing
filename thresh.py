import cv2 as cv

img= cv.imread('D:\\Picture of Rifat & video\\lion.jpg')
#cv.imshow('lion', img)

#convrt to gray 
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#simple Thresholding 
threshold, thresh = cv.threshold(gray, 100, 150, cv.THRESH_BINARY)
cv.imshow('Thredhold',thresh)

#addapted threshold 
adap_thres = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive',adap_thres)

adap_thres1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive',adap_thres1)

adap_thres2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive',adap_thres2)

cv.waitKey(0)