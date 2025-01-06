# YOLOv5 RTSP Object Detection

This project implements object detection using the YOLOv5 model on an RTSP video stream. It connects to an RTSP stream, processes the frames, and applies the YOLOv5 model to detect and display objects in real-time.

## Project Structure

```
yolov5-rtsp
├── src
│   ├── detect.py       # Main script for object detection
│   └── utils.py        # Utility functions for processing
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yolov5-rtsp.git
   cd yolov5-rtsp
   ```

2. **Install dependencies:**
   Make sure you have Python 3.6 or higher installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the RTSP stream:**
   Update the RTSP URL in `src/detect.py` to point to your camera stream.

## Usage

To run the object detection script, execute the following command:
```bash
python src/detect.py
```

## YOLOv5 Model

This project utilizes the YOLOv5 model for object detection. For more information about YOLOv5, visit the [YOLOv5 GitHub repository](https://github.com/ultralytics/yolov5).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.