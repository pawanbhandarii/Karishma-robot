# importing libraries
import cv2
import numpy as np

check = False
start = 0

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('RE.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False):
	print("Error opening video file")

# Read until video is completed
while (cap.isOpened()):

# Capture frame-by-frame
	ret, frame = cap.read()
	if ret == True:
		cv2.imshow('Frame', frame)
    else:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
       continue

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
