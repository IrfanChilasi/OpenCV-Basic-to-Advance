import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")

if (cap.isOpened() == False):

    #Indicator
    print("Error in loading video")


#Reading and playing
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Video", frame)
        cv.waitKey(0) & 0xFF == ord('q')
        break
    else:
        break
cap.release()
cv.destroyAllWindows()