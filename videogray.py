#Converting Video to Gray or Black and White 
from tkinter import Frame
import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    
    #to show in player
    if ret == True:
        cv.imshow("Video", binary)
        #to quit with "q" key
        cv.waitKey(0) & 0xFF == ord("q")
        break
    else:
        break
cap.release()
cv.destroyAllWindows()