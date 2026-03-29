import cv2 as cv
import numpy as np

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /cat1.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh' ,thresh)

contours , hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contour show', blank)


'''
the modes you can pass in above line is 
cv.RETR_EXTERNAL → only outer contours
cv.RETR_LIST → all contours
cv.RETR_TREE → hierarchy included
the methods you can pass 
cv.CHAIN_APPROX_SIMPLE → efficient (better)
cv.CHAIN_APPROX_NONE → stores all points (heavy)
'''
cv.waitKey(0)