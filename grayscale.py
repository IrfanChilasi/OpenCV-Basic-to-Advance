#Gray Scale COnversion
import cv2 as cv
from cv2 import cvtColor
img = cv.imread("resources/image.jpg")
img = cv.resize(img, (600, 400))

#Conversion
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)

#Display code
cv.imshow("First Image", img)
cv.imshow("First Image", gray_img)

#Delay Code
cv.waitKey(0)
cv.destroyAllWindows()