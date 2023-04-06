import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

segmentor = SelfiSegmentation()
fps_reader = cvzone.FPS()

# Define a list of background images
bg_dir = "images/"
bg_images = [os.path.join(bg_dir, file) for file in os.listdir(bg_dir) if file.endswith('.jpg')]

bg_index = 0 # Initialize the background index to 0

imgBg = cv2.imread(bg_images[bg_index])
imgBg = cv2.resize(imgBg, (640, 480)) # Resize the background image to match the input image dimensions

while True:
    success,img = cap.read()
    img = cv2.resize(img, (640, 480)) # Resize img to match the video dimensions

    img_out = segmentor.removeBG(img,imgBg,threshold=0.8)
    img_out = cv2.resize(img_out, (640, 480)) # Resize img_out to match the video dimensions

    img_stacked = cvzone.stackImages([img,img_out],2,1)
    _, img_stacked = fps_reader.update(img_stacked,color=(0,0,255))

    cv2.imshow('image',img_stacked)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('n'): # If the user presses 'n', switch to the next background image
        bg_index = (bg_index + 1) % len(bg_images)
        imgBg = cv2.imread(bg_images[bg_index])
        imgBg = cv2.resize(imgBg, (640, 480)) # Resize the background image to match the input image dimensions

    elif key == ord('b'): # If the user presses 'b', switch to the previous background image
        bg_index = (bg_index - 1) % len(bg_images)
        imgBg = cv2.imread(bg_images[bg_index])
        imgBg = cv2.resize(imgBg, (640, 480))

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()