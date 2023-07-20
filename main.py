import pyautogui
import cv2
import numpy as np


#///////////////////////////////////////////////////////////////
#resolution specified
resolution =(1920,1080)

#video codec specified
codec = cv2.VideoWriter_fourcc(*"XVID")

#output file name speicify
filename = "recording.avi"

#speify frame rate
fps =60.0

#Creating a videowriter project
out=cv2.VideoWriter(filename, codec, fps, resolution)

#//////////////////////////////////////////////////////////////

#create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

#Resize this windows
cv2.resizeWindow("Live", 480, 270)



while True:

  #take screenshot using PyAutoGUI
  img = pyautogui.screenshot()

  #convert the screenshot to an numpy array
  frame = np.array(img)

  #convert it from BGR(Blue, Green, Red) to RGB
  frame =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  #WRITE it to the output file
  out.write(frame)

  #Display the recording screen
  cv2.imshow('Live', frame)

  #stop recording when we press q
  if cv2.waitkey(1) == ord('q'):
    break

#release the video writer
out.release()

#destroy all winodws
cv2.destroyAllWindows()
