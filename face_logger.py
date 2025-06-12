import cv2
import time
from datetime import datetime

# Initialize the face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open webcam
cap = cv2.VideoCapture(0)

# Create a log file
log_file = open("face_log.txt", "a")

print("Press 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles and log faces
    for (x, y, w, h) in faces:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Face detected at X:{x}, Y:{y}, W:{w}, H:{h}\n")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show video feed
    cv2.imshow("Face Logger", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
log_file.close()
