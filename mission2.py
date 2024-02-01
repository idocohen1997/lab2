import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)
ret , frame = vid.read()
r=0
g=0
b=0

while True:
    cv.imshow('mission2',frame)
    A=cv.waitKey(1)
    if A & 0xFF == ord('r'):
        r_pre=r
        g_pre=g
        b_pre=b
        r=100
        g=0
        b=0
        frame = cv.add(frame,(b-b_pre,g-g_pre,r-r_pre,0))
    elif A & 0xFF == ord('b'):
        r_pre=r
        g_pre=g
        b_pre=b
        r=0
        g=0
        b=100
        frame = cv.add(frame,(b-b_pre,g-g_pre,r-r_pre,0))
    elif A & 0xFF == ord('g'):
        r_pre=r
        g_pre=g
        b_pre=b
        r=0
        g=100
        b=0
        frame = cv.add(frame,(b-b_pre,g-g_pre,r-r_pre,0))
    elif A & 0xFF == ord('g'):
        r_pre=r
        g_pre=g
        b_pre=b
        r=0
        g=100
        b=0
        frame = cv.add(frame,(b-b_pre,g-g_pre,r-r_pre,0))
    elif A & 0xFF == ord('v'):
        r_pre=r
        g_pre=g
        b_pre=b
        r=100
        g=0
        b=100
        frame = cv.add(frame,(b-b_pre,g-g_pre,r-r_pre,0))
    elif A & 0xFF == ord('s'):
        cv.imwrite("photo_l2m2.jpg",frame)
    elif A & 0xFF == ord('q'):
        break