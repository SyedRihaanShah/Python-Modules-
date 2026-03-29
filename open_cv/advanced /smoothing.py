import cv2 as cv

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /cat3.jpg')

cv.imshow('cat', img)

#averaging
#simple blur and poor edge preservation
average = cv.blur(img, (15,15))
cv.imshow('Average', average)

#gausain blur 
#general purpose and moderate edge preservation
gauss = cv.GaussianBlur(img, (15,15), sigmaX=0)
cv.imshow('gauss', gauss)

#median blur
#best for salt and pepper noise 
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

#bilateral blur
#best for edge preservation but slow
bilaterl = cv.bilateralFilter(img , 20, sigmaColor = 50, sigmaSpace=40)
cv.imshow('bilateral', bilaterl)

cv.waitKey(0)