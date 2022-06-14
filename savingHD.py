#Saving Hd recording of cam streaming 
from tkinter import Frame
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
#Setting Resolution HD (1280 x 720)



def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)

def fhd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)

#hd_resolution()
fhd_resolution()
#writing format, video write object and file output

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),10, (frame_width, frame_height), isColor=False)


while (True):
    (ret, frame) = cap.read()

    #to show in player
    if ret == True:
        out.write(frame)
        cv.imshow("Video", frame)
        #to quit with "q" key
        if cv.waitKey(1) & 0xFF == ord('q'):
           break

    else:

        break

cap.release()
cv.destroyAllWindows()    