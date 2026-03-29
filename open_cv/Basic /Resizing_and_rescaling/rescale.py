import cv2 as cv 

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /cat3.jpg')

cv.imshow('cat', img)


def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_NEAREST)


resized_image = rescaleFrame(img)
cv.imshow('ReImage', resized_image)

def changeRes(width,height):#only for live vids 
    capture.set(3, width)#3 stands for width 
    capture.set(4, height)#4 stands for height



capture = cv.VideoCapture('/Users/syedrihaanshah/Python-Modules-/open_cv/vidoes /mixkit-pet-owner-playing-with-a-cute-cat-1779-hd-ready.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video_2', frame_resize)


    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# when we zoom, flip or do any any operation on a frame new gaps are formed these gaps are filled by interpolation
# Types:
# INTER_NEAREST -> picks the nearest pixel, fast but less image quality 
# INTER_LINEAR -> uses 4 nearby pixels , smooth and balanced 
# INTER_CUBIC -> uses 16 nearby pixels , slower but better quality 
# INTER_AREA -> best for shriking images , redcues noise and aliasing 

# cv.waitKey(0)