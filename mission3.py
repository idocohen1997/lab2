import cv2 as cv
import numpy as np
frame = cv.imread("photo_l2m2.jpg")
sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
gauss = np.array([[1,2,1],[2,4,2],[1,2,1]])
scalar = 1/16
rotem = np.dot(gauss,scalar)

frame2 = cv.filter2D(frame,-1,sharpen)
gauss_frame = cv.filter2D(frame,-1,rotem)
subtract = cv.subtract(frame,gauss_frame)
multiply = cv.multiply(subtract,8.1)
frame3 = cv.add(frame,multiply)
#frame3 = frame - 0.8*(frame - gauss_frame)
while True:
    cv.imshow('original',frame)
    cv.imshow('sharpen',frame2)
    cv.imshow('gauss_frame',gauss_frame)
    cv.imshow('subtract',subtract)
    cv.imshow('multiply',multiply)
    cv.imshow('gauss',frame3)
    A=cv.waitKey(1)
    if A & 0xFF == ord('q'):
        break