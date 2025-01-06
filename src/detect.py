# Contents of /yolov5-object-detection/yolov5-object-detection/src/detect.py

import cv2
import torch
import time

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load the YOLOv5s model

# RTSP stream URL
rtsp_url = 'rtsp://admin:PZAVKH@192.168.1.2:554/channel0'

# Start capturing the video stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open RTSP stream.")
    exit()

frame_skip = 5  # Process every 5th frame
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    # Perform object detection
    results = model(frame)

    # Render results on the frame
    frame = results.render()[0]

    # Resize the frame to fit within the display window
    frame = cv2.resize(frame, (800, 600))  # Adjust the size as needed

    # Display the frame with detections
    cv2.imshow('YOLOv5 Object Detection', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Add a small delay to reduce the frame rate
    time.sleep(0.1)

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()