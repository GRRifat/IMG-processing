import os
import cv2 as cv
import numpy as np

people = ['messi','neymar','Ronaldo','Rumi']
DIR= r'D:\Picture of Rifat & video\face'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

feature = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            face_rects = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in face_rects:
                faces_roi = gray[y:y+h,x:x+w]
                feature.append(faces_roi)
                labels.append(label)

create_train()
print('training done')
feature = np.array(feature,dtype='object')
labels = np.array(labels)


# print(f'len={len(feature)}')
# print(f'len={len(labels)}')

faces_recognizer = cv.face.LBPHFaceRecognizer_create()
# train the model
faces_recognizer.train(feature,labels)

faces_recognizer.save('face_trained.yml')

np.save('feature.npy',feature)
np.save('labels.npy',labels)
