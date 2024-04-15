# Motion Detection Security Camera

This Python program uses OpenCV to detect motion through a webcam. When motion is detected, the area with motion is highlighted and the background is changed to red.

## Prerequisites

Before you run this program, you need to have Python installed on your system. The program also depends on the following Python libraries:
- OpenCV
- Numpy

You can install them using pip:

```bash
pip install opencv-python numpy
```
Clone this repository to your local machine:
```bash
git clone <https://github.com/Opirel/opencv_securityCam.git>
```

Navigate to the project directory:
```bash
cd opencv_securityCam
```

Run the program: 
```bash
python app.py
```



The program will activate the primary webcam. Keep the webcam stable and point it towards the area you want to monitor for motion.

How It Works
The program captures video from the webcam.
It processes each frame to detect changes/movements using OpenCV functions.
If motion is detected in a frame, it highlights the area of motion and changes the background of this area to red.
Configuration
You can adjust the sensitivity of motion detection by modifying the following parameters in the code:

    threshold value in the cv2.threshold() function.
    minimum area of contours considered as valid motion.
    kernel size for GaussianBlur to manage the level of detail.
    iterations in cv2.dilate() to manage the connection of adjacent contour regions.
    Quitting the Program
    Press 'q' while the program window is active to safely close the program and release the webcam.





