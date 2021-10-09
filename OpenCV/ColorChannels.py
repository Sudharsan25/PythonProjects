import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow("Group",img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# Split Color channels
b, g ,r = cv.split(img)
# To display the color channels in grayscale
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
# To display the images in their own color channels
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,g])
cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

# merge color channels
mergred = cv.merge([b,g,r])
cv.imshow("Merged",mergred)

cv.waitKey(0)