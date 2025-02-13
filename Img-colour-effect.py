import cv2 as cv 

img= cv.imread('D:\\Picture of Rifat & video\\im.jpg')

cv.imshow('im', img)

#convrt to gray 
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)

#Edge Coscode 
canny = cv.Canny(img,50,200)
cv.imshow('EDge',canny)

#dilating the img
dilated = cv.dilate(canny,(5,5),iterations=1)
cv.imshow('Dilated',dilated)

#Resized
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# #Cropping
# cropped= img(50:100,100:200)
# cv.imshow('Cropped',cropped)
cv.waitKey(0)