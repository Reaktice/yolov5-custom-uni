def preprocess_frame(frame):
    # Resize and normalize the frame for YOLOv5
    frame = cv2.resize(frame, (640, 640))
    frame = frame / 255.0  # Normalize to [0, 1]
    return frame

def postprocess_detections(detections, conf_threshold=0.4):
    # Filter detections based on confidence threshold
    filtered_detections = []
    for detection in detections:
        if detection[4] >= conf_threshold:  # Confidence score
            filtered_detections.append(detection)
    return filtered_detections

def handle_video_stream(rtsp_url):
    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)
    if not cap.isOpened():
        raise Exception("Could not open video stream")
    return cap

def release_video_stream(cap):
    # Release the video capture object
    cap.release()