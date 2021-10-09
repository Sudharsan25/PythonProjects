import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Boston',img)

# translating - changin the x and y axis of the image
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x => Shift left
# -y => Shift right
# x => Shift up
# y => Shift down

translate = translate(img,100,100)
cv.imshow('Translated',translate)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (height,width)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow("Rotated",rotated)

# Resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC) ### We can use INTER_LINEAR to enlarge image
cv.imshow("Resized",resized)

# Flipping
# 0 => flip vertically
# 1 => flip horizontaly
# -1 => flip both veritcally and horizontally
flip = cv.flip(img, 0)
cv.imshow('Flipped',flip)

cv.waitKey(0)