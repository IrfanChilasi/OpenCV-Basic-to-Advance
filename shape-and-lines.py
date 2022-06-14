# How o draw shapes and lines in Python
import cv2 as cv
import numpy as np

#Draw Canvas
img = np.zeros((600,600)) #zeros for Black
img1 = np.ones((600,600)) #ones for White
#Print Size
print("The size of our canvas is: ", img.shape)

#Adding colors to the canvas
colored_img = np.zeros((600,600, 3), np.uint8) #Addition of color channels
colored_img[:] = 225,0,245 #color for complete image
colored_img[150: 210, 100:200] = 111,111,111  #TO color a part of image

#Adding line
cv.line(colored_img, (0,0), (700,700), (255,0,140), 3)

#Adding REctangles
cv.rectangle(colored_img, (50,100), (300,400), (255,240,0), 3) #Draw
cv.rectangle(colored_img, (50,100), (300,400), (255,240,0), cv.FILLED) #Filled

#Adding Circle
cv.circle(colored_img, (400,300), 50, (255,100,0), 5)
cv.circle(colored_img, (400,300), 50, (255,100,0), cv.FILLED)

#Adding Text
cv.putText(colored_img, "Let's learn OpenCV ", (200,500),cv.FONT_HERSHEY_COMPLEX, 1,(255,255,0),2)


#cv.imshow("Black", img)
#cv.imshow("White", img1)
cv.imshow("Colored", colored_img)
cv.waitKey(0)
cv.destroyAllWindows()