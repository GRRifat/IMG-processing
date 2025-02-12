import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['messi','neymar','Ronaldo','Rumi']
# feature=np.load('feature.npy')
# labels=np.load('labels.npy')

faces_recognizer = cv.face.LBPHFaceRecognizer_create()
faces_recognizer.read('face_trained.yml')

img=cv.imread(r"D:\Picture of Rifat & video\face\n\mes.jpg")


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)


faces_rect= haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    face_roi=gray[y:y+h,x:x+w]
    label,confidence=faces_recognizer.predict(face_roi)
    print(f'Label={people[label]}\nConfidence={confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)