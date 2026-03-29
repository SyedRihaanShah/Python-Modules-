import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images /cat3.jpg')

cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show()

#BGR to gray scale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#BGR to HSV(hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)

#lab to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('lab_bgr', lab_bgr)



# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)