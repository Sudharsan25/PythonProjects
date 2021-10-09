import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Photos/lady.jpg')

# plt.imshow(img)
# plt.show()
### We can see a huge difference in the image because matplotlib doesn't know to display BGR images
### Whereas , OpenCV reads all images and displays it in BGR format

cv.imshow('Lady',img)

# Convert BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Convert BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# Convert BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
# Similar image was displayed by matplotlib
# But look what happens when we display a RGB Image in matplotlib
plt.imshow(rgb)
plt.show()

# Also if you wish to convert from one color space to another
# Like HSV to LAB , then you have to convert HSV to BGR first
# and then convert that BGR to LAB. There is no direct convertion
# In OpenCV

cv.waitKey(0)