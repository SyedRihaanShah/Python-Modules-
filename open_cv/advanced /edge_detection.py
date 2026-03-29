import cv2 as cv
import numpy as np

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /park.jpg' )
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#laplacian
lap = cv.Laplacian(gray, ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0 , 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('SobelX', sobelx)
cv.imshow('Sobely', sobely)
cv.imshow('combined_sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)


cv.waitKey(0)