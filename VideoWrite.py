#Writing Video from cam
from tkinter import Frame
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#writing format, video write object and file output

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),10, (frame_width, frame_height), isColor=False)
while (True):
    (ret, frame) = cap.read()

    #For grayscale video
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #to show in player
    if ret == True:
        out.write(gray_frame)
        cv.imshow("Video", gray_frame)
        #to quit with "q" key
        if cv.waitKey(1) & 0xFF == ord('q'):
           break

    else:

        break
    
cap.release()
out.release()
cv.destroyAllWindows()