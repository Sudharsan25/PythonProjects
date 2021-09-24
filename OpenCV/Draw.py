import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype="uint8")

### painting the image

# Color the whole
blank[:]= 0,255,0
# Color specific parts of image
blank[200:300,300:400] = 0,255,255

# Draw shapes
#Giving the size Explicitly
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
# Using the shape
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=-1)

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=3)
# Fill the shapes by giving thickness as -1
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=-1)

cv.line(blank, (0,0) , (blank.shape[1]//2,blank.shape[0]//2) ,(255,255,255) ,thickness=3)

# Write text
cv.putText(blank,"Hello",(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)

cv.imshow('Blank',blank)

cv.waitKey(0)




