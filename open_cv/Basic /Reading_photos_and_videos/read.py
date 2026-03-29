import cv2 as cv 


#Reading images 
# img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/Reading_photos_and_videos/images /cat1.jpg')
#imread takes a arg of path of the file and returns a matrix of pixels 

# cv.imshow('Cat', img)
#takes two arg one is window name and other is the matrix of pixels to display 


#reading Videos 

capture = cv.VideoCapture('/Users/syedrihaanshah/Python-Modules-/open_cv/Reading_photos_and_videos/vidoes /mixkit-pet-owner-playing-with-a-cute-cat-1779-hd-ready.mp4')
#0 -> your webcam 

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
#waits for a certain time in ms unit a key is pressed and 0 means infinite time 