import cv2 as cv

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /cat1.jpg')
cv.imshow("cat", img)

#converting to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

#blurring a image 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade 
cany = cv.Canny(blur, 125, 175)
cv.imshow('canny', cany)
#converts the img in such a form of blackoutine where there is a edge

#dilating a image 
dilated = cv.dilate(cany, (7,7), iterations=5)
cv.imshow('Dialated', dilated)

#eroding 
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#cropping 
croped = img[50 : 200,  200:400]
cv.imshow('cropped', croped)
cv.waitKey(0)