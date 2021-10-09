import cv2 as cv

img = cv.imread('Photos.cat_large.png')

### Rescaling Images ,Videos and Live videos

def rescale(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')

### Resizing only live videos

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)



while True:
    isTrue, frame = capture.read()

    frame_resized = rescale(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video_resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
