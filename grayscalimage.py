
import cv2
image=cv2.imread('dhoni.jpeg')
imageGI=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('color',image)
cv2.imshow('grayscal',imageGI)
cv.waitkey(0)
