#Gray Scale COnversion
import cv2 as cv
from cv2 import cvtColor
from cv2 import imwrite
img = cv.imread("resources/irfan.png")
img = cv.resize(img, (600, 400))

#Conversion
gray = cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
#Display code
imwrite('resources/Image_gray.png', gray)
imwrite('resources/Image_bw.png',binary)

#Delay Code
# cv.waitKey(0)
# cv.destroyAllWindows()