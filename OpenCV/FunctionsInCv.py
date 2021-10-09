import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)


# Converting to GreyScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur
blur = cv.GaussianBlur(img, (7,7) ,cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge cascade
cany = cv.Canny(img,125,175)
cv.imshow('Canny', cany)

# Dialating the image
dilated =cv.dilate(cany,(3,3),iterations=1)
cv.imshow("Dialted",dilated)

# Eroding - Restore the image before dialting
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("Eroded",eroded)

# Resize
resized = cv.resize(img,(500,500))
cv.imshow("Resized",resized)

cv.waitKey(0)