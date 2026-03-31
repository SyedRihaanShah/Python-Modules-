import cv2 as cv

cap = cv.VideoCapture(0)

#Function to get properties of video capture object 
# width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
# fps = cap.get(cv.CAP_PROP_FPS)
# brightness = cap.get(cv.CAP_PROP_BRIGHTNESS)q
# print(brightness)

#to set properties 
cap.set(cv.CAP_PROP_FRAME_WIDTH, 200)

while True:
    ret, frame = cap.read()

    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()