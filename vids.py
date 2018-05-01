import cv2
import numpy as np
cap=cv2.VideoCapture(1)
while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    