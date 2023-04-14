# Background Removal using SelfiSegmentation
This code demonstrates the use of the SelfiSegmentation module from the cvzone library to remove the background from a video stream in real-time.


## Requirements
* Python 3
* OpenCV
* cvzone


## Usage
1. Clone the repository and navigate to the directory containing the code.
2. Install the required libraries using *pip install -r requirements.txt*.
3. Place the background images you want to use in the *images/* directory. The images should be in *.jpg* format.
4. Run the script using *python background_removal.py*.
5. Press 'n' to switch to the next background image and 'b' to switch to the previous one.
6. Press 'q' to exit the program.


## Explanation
* The cv2.VideoCapture() function is used to create a video capture object that captures frames from the default camera.
* The SelfiSegmentation class is used to create an instance of the SelfiSegmentation module, which is used to remove the background from the input frames.
* The cvzone.FPS() class is used to create an instance of the FPS module, which is used to measure the frames per second of the output video.
* The background images are loaded from the images/ directory using the os library and stored in a list.
* A while loop is used to capture frames from the video stream, process them using the SelfiSegmentation module, and display the output.
* The cvzone.stackImages() function is used to stack the input and output frames vertically, and the cvzone.FPS().update() function is used to update the FPS counter.
* The program responds to the user pressing 'n' or 'b' to switch between background images and 'q' to exit the program.
* Finally, the video capture object is released and the windows are closed.
