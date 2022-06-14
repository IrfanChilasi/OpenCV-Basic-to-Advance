#Gray Scale COnversion
import cv2 as cv
from cv2 import cvtColor
img = cv.imread("resources/irfan.png")
img = cv.resize(img, (600, 400))

#Conversion
gray = cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
#Display code
cv.imshow("orginal", img)
cv.imshow("gray", gray)
cv.imshow("Black and White", binary)

#Delay Code
cv.waitKey(0)
cv.destroyAllWindows()