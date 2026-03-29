import cv2 as cv
import numpy as np

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /cat3.jpg')
cv.imshow('cat', img)

blank = np.zeros(img.shape[0:2], dtype='uint8')
cv.imshow('blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2   ), 500, 255, -1)
cv.imshow('mask', mask)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked_img', masked_img)

cv.waitKey(0)