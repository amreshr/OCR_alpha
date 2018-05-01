import cv2
import numpy as np
import matplotlib.pyplot as plt
'''img=cv2.imread('watch2.jpg',cv2.IMREAD_GRAYSCALE)
#Imread_color=1
#imread_Unchanged=-1
cv2.imshow('image',cv2.imread('watch2.jpg',cv2.IMREAD_GRAYSCALE))
cv2.waitKey(0)
cv2.destroy
byteArray = bytearray(img)'''

#plt.imshow(img,cmap='gray',interpolation='bicubic')
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    pink=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lol=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    kool=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('pink',pink)
    cv2.imshow('lol',lol)
    cv2.imshow('kool', kool)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

