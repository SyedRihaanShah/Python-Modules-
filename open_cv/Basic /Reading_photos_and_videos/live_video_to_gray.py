import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)#here 0 is passed to get my webcam
if not cap.isOpened():#checks wether the camera is opened
    print('Cannot open camera ')
    exit()
while True:
    #captures frame by frame 
    ret, frame = cap.read() #here we use 2 variables as read returns a tuple of bool and a array

    #if frame is read properly ret is true 
    if not ret :
        print("cant receive frame ")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('gray frame', gray)
    if cv.waitKey(1) == ord('q'):
        break 

#to release the capture 
cap.release()
cv.destroyAllWindows()

