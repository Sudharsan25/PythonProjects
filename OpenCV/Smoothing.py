import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat',img)

# Averaging
average = cv.blur(img,(3,3)) # Higher the kernel size , more the blur
cv.imshow("Avg Blur",average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3),0)
cv.imshow("Gaussian Blur",gauss)
# We can see that Gaussian Blur gives the image more natural blur than Averaging

# Median Blurring
median = cv.medianBlur(img,3)
cv.imshow("Median Blur",median)
# Median blurring reduces noise in the image more efficiently . But it is not used for high kernel sizes

# Bilateral Blurring
# One specific advatange of Bilateral blurring is that it retains the edges of the image before blurring
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)