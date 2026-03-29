import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/Users/syedrihaanshah/Python-Modules-/open_cv/images /cat3.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 250, 255, -1)
# cv.imshow('mask', circle)

masked_img = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('masked', masked_img)

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0],mask=circle, histSize=[256], ranges=[0,256])

plt.figure()
plt.title('Gray scale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixles')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)