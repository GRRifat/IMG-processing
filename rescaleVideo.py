import cv2 as cv 
capture=cv.VideoCapture('D:\Picture of Rifat & video\\coxs.mp4')


def rescaleframe(frame , scale=0.75):
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0]* scale)

    dismentions = (width,height)
    return cv.resize(frame,dismentions,interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleframe(frame)
    cv.imshow('coxs',frame)
    cv.imshow('video Resized',frame_resized)

    if  cv.waitKey(20) & 0xFF==ord ('a'):
        break
    

capture.release()
cv.destroyAllWindows()

