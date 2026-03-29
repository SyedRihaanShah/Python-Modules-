import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (20,20), (370,370), color=255, thickness=-1)
circle = cv.circle(blank.copy(), (200,200), radius=200, color=255, thickness=-1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise AND -> intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_and)

#bitwise OR -> intersecting and non intersecting region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

#bitwise XOR -> non intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

#bitwise NOT 
bitwise_Not = cv.bitwise_not(rectangle)
cv.imshow('Not', bitwise_Not)
cv.waitKey(0)