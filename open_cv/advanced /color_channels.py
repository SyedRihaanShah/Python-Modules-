import cv2 as cv
import numpy as np

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /park.jpg')
cv.imshow('park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b, g, r = cv.split(img)
blue = cv.merge([b,blank,blank])
cv.imshow('blue', blue)
green = cv.merge([blank, g, blank])
cv.imshow('green', green)
red = cv.merge([blank, blank, r])
cv.imshow('red', red)

# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r)  

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge = cv.merge([b,g,r])
cv.imshow('merged', merge)

cv.waitKey(0)