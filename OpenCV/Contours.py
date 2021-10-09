import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow("Cats",img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("blank",blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow("Canny",canny)

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)
# Thresholding just binarizes images

contours, hireachies = cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.fincontours returns a list of all co ordinates of the contours and Hireachy - which represents the hireachy of the contour
print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contours",blank)

cv.waitKey(0)