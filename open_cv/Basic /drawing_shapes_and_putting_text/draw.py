import cv2 as cv 
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#paint the img a certain color 
blank[200:300 , 300:400] = 0,0,255
cv.imshow('Green', blank)

#draw a rectangle 
# cv.rectangle(blank, (0,0), (blank.shape[1]//2 , blank.shape[0]//2), (0,255,0), thickness=-1)
#to fill the rectangle you can use -1 or cv.filled in thickness 
#to get border use +ve int in thickness 
# cv.imshow('Rectangle', blank)

#draw a circle 
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness= -1 )
# cv.imshow('CIRCLE', blank)

# #draw a line 
# cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),  (255,255,255), thickness= 3)
# cv.imshow('Line', blank)

#write text 
cv.putText(blank, 'hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 2)
cv.imshow('text', blank)

cv.waitKey(0)
#BGR 