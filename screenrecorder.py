# Simple screen recorder

import cv2
import numpy as np
import pyautogui

output = "screen_record.mp4"

# get info from pic
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
height, width, channels = image.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 8.0, (width, height))

# Creating a live preview window
cv2.namedWindow("Rec-Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rec-Live", 800, 500)

while True:
    try:
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        out.write(image)
        # Display the recording screen
        cv2.imshow('Rec-Live', image)
        StopIteration(0.5)
        # Stop recording when we press 'q'
        if cv2.waitKey(1) == ord('q'):
            print(f"Recording stopped...File saved as {output}")
            break

    except KeyboardInterrupt:
        print(f"Recording stopped...File saved as {output}")
        break

out.release()
cv2.destroyAllWindows()