import cv2 as cv
import numpy as np

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /cat3.jpg')
cv.imshow('cat', img)

#translation
#which means moving image left right up and down or in x and y axis 
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

#if x = -ve -> left 
#if y = -ve -> up 
translated = translate(img, 50, 60)
cv.imshow('translated', translated)

#rotation 
def rotate(img, angle ,rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)
# +ve angle -> counterclockwise 

#flipping
flip = cv.flip(img, 1)
#it takes two arguments one is frame and other is flipcode 
#if flipcode is 0 flip vertically or upside down 
#flipcode is 1 flip horizontally or mirror
#flipcdoe is -1 flip both axes or rotate 180 deg
cv.imshow('flip', flip)

#cropping 
cropped = img[200: 400, 300 : 400]
cv.imshow('cropped', cropped)


cv.waitKey(0)