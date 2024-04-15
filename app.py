import cv2
import numpy as np


cap = cv2.VideoCapture(0)  # Use 0 for the primary webcam

# Read the first frame
ret, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)



while True:
    # Read the next frame
    ret, frame2 = cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
    
    # Calculate the difference between each frame
    delta = cv2.absdiff(gray1, gray2)
    threshold = cv2.threshold(delta, 20, 255, cv2.THRESH_BINARY)[1] #default (delta, 25, 255, cv2.THRESH_BINARY
    threshold = cv2.dilate(threshold, None, iterations=2)
    
    # Find contours to detect movements
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        # If significant movement is detected, change the background
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.fillPoly(frame2, pts =[contour], color=(0,0,255))
    
    # Display the resulting frame
    cv2.imshow('frame', frame2)
    if cv2.waitKey(1) == ord('q'):
        break

    # Update the first frame
    gray1 = gray2

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()