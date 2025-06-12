# OpenCV Haar Cascade Face Detection Project

This project demonstrates face detection using OpenCV's Haar cascade classifier. It supports both real-time webcam logging and static image analysis, with the ability to log detections and save face snapshots.

## 🚀 Features

- Face detection using Haar cascades
- Real-time webcam analysis with green bounding boxes
- Snapshot saving to local folder with timestamps
- Static image detection mode with basic AI-style decision logic
- Compatible with both **Windows** and **Linux (Ubuntu)** environments

## 🧪 Files

| File | Description |
|------|-------------|
| `face_logger.py` | Uses webcam input, logs faces, draws boxes, saves snapshots |
| `haar_detector.py` | Analyzes a test image and prints "AI decision" |
| `haarcascade_frontalface_default.xml` | Haar cascade configuration from OpenCV |
| `test_face.jpg` | Sample test image for static analysis |
| `face_log.txt` | Log of timestamps and bounding box coordinates |
| `face_snapshots/` | Folder for storing cropped face images |

## 🖥️ Setup & Requirements

- Python 3.10+
- OpenCV installed:  
  ```bash
  pip install opencv-python
