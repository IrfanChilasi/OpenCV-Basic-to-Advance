#import libraries
import cv2 as cv
img = cv.imread("resources/image.jpg")
img = cv.resize(img, (600, 400))
#img = cv.imread(resources/image.jpg)
cv.imshow("First Image", img)
cv.waitKey(0)