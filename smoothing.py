import cv2 as cv 

img= cv.imread('D:\\Picture of Rifat & video\\park.jpg')
cv.imshow('park', img)


#Averaging.
average = cv.blur(img, (3,3))
cv.imshow('Average',average)

#Gauss Blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur', gauss)

#Bilateral 
bilateral = cv.bilateralFilter(img , 5, 15 , 15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)