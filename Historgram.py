import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('D:\\Picture of Rifat & video\\lion.jpg')
cv.imshow('lion', img)




blank= np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('Blank',blank)

# #convrt to gray 
# gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# gray_hist= cv.calcHist([gray],[0],None,[256],[0,256])


mask = cv.circle(blank,(img.shape[1]//2 -20, img.shape[0]//2 -20),100, 255, -1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)

# plt.figure()
# plt.title('Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,255])
# plt.show()

#colour HIstogram 
plt.figure()
plt.title('Colour - Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
colors = ('b', 'g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()