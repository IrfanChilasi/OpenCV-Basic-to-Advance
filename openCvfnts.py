#basic function and manupulation in openCV
import cv2 as cv
from cv2 import blur
from cv2 import resize
import numpy as np

img = cv.imread("resources/image.jpg")
#resize
blur_img = cv.resize(img,(23,23), 0)

#edge detection
edge_img = cv.Canny(img,48,48)

#Thickness of Lines
mat_kernal = np.ones((7,7), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernal), iterations=1) #iteration is coating of paints

#Make Thinner outlines
ero_img = cv.erode(dilated_img, mat_kernal, iterations=1)

#cropping we will use numpy not OpenCV
print("The size of pur Image is:", img.shape)
cropped_img = img[0:200,200:300]


cv.imshow("Original", img)

#Make Black and White image
cv.imshow("Blur", blur_img)
cv.imshow("edge", edge_img)
cv.imshow("Dilated", dilated_img)
cv.imshow("Erosion", ero_img)
cv.imshow("Cropped", cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()