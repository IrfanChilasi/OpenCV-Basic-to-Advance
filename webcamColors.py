#Convert webcam into Different Colors in Python
import cv2 as cv
from matplotlib.pyplot import gray
import numpy as np

#read the frame from the camera
cap = cv.VideoCapture(0) #webcam no =1

#read untill the end
while(cap.isOpened()):
    #Capture frame by frame
    ret, frame = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)
    cv.imshow("OrginalCam", frame)
    cv.imshow("GrayCam", gray_frame)
    cv.imshow("BinaryCam", binary)

    #To quit with 'q' key
    if cv.waitKey(1) & 0xFF == ord("q"):
      break
cap.release()
cv.destroyAllWindows()
