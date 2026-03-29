import cv2 as cv

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /group.jpg')
cv.imshow('faces', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('/Users/syedrihaanshah/Python-Modules-/open_cv/Faces/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10)

print(f'number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=6)

cv.imshow('Detected', img)

cv.waitKey(0)
'''
scale facotr = the image is repeatedly shrunk to detect faces of different sizes. 
1.05 - > very detailed(slow but accurate)
1.1 - > balanced 
1.3 -> fast but misses 
smaller scale factor = more zoom levels = better detection
minNeighbors = a detection is accepted only if multiple nearby rectangles agree 
'''