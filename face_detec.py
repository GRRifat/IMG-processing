import cv2 as cv

img= cv.imread("D:\\Picture of Rifat & video\\team.jpg")
cv.imshow('ar',img)


#convrt to gray 
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=3)

print(f'Face found: {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0),thickness=2)

cv.imshow('Detected Faces ',img)
cv.waitKey(0)