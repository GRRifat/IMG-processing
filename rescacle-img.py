import cv2 as cv

img = cv.imread('D:\\Picture of Rifat & video\\rifat.jpg')
cv.imshow('rifat',img)

def rescaleframe(frame , scale=0.75):
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0]* scale)

    dismentions = (width,height)
    return cv.resize(frame,dismentions,interpolation=cv.INTER_AREA)

resizes_image = rescaleframe(img)
cv.imshow('Resizes Image',resizes_image)
cv.waitKey(0)