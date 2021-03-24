# Records video until user presses 'q' and then saves the video

import numpy as np
import cv2

fps = 20.0
width = 640
height = 480
output = 'camcap.mp4'

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, fps,(width,height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        out.write(frame)
        cv2.imshow('output', frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()