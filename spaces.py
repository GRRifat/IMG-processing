import cv2 as cv 
import matplotlib.pyplot as plt

img= cv.imread('D:\\Picture of Rifat & video\\im.jpg')
cv.imshow('im', img)

plt.imshow(img)
plt.show()

# #convrt to gray 
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*G*R
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('BGR to RGB',rgb)

# plt.imshow(img)
# plt.show(rgb)

cv.waitKey(0)