import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)
ret , frame = vid.read()

while True:
    cv.imshow('mission1',frame)
    A=cv.waitKey(1)
    if A & 0xFF == ord('w'):
        frame = cv.add(frame,(10,10,10,0))
    elif A & 0xFF == ord('x'):
        frame = cv.add(frame,(-10,-10,-10,0))
    elif A & 0xFF == ord('a'):
        frame = cv.multiply(frame,(1.3,1.6,1.9,0))
    elif A & 0xFF == ord('d'):
        frame = cv.multiply(frame,(0.769,0.625,0.526,0))
    elif A & 0xFF == ord('s'):
        cv.imwrite("photo_l2m1.jpg",frame)
    elif A & 0xFF == ord('q'):
        break