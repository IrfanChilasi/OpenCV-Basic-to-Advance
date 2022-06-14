#How to capture a webcam in Python
import cv2 as cv
import numpy as np

#read the frame from the camera
cap = cv.VideoCapture(0) #webcam no =1

#read untill the end
while(cap.isOpened()):
    #Capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # To duisplay frames
        cv.imshow("Frame", frame)
        #To quit with 'q' key
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
