import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
ret,frame = cap.read()
fps = cap.get(cv.CAP_PROP_FPS)

#Define the codec and creating a videowriter 
h,w = frame.shape[:2]
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc=fourcc, fps=fps, frameSize=(w,h))



while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Cant recieve frame")
        break
    # frame = cv.flip(frame,0)
    #flipe is used to flip image vertically and horizontally 
    #1 - > horizontally and 0-> vertically and -1  - > both axes 

    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()