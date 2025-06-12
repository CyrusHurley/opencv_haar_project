import cv2

# Load pre-trained Haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load test image
img = cv2.imread('test_face.jpg')
if img is None:
    print("Error: Image not found.")
    exit(1)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Decision logic
if len(faces) > 0:
    print("✅ FACE DETECTED")
    print("ACTION: Triggering movement flag or AI routine...")
else:
    print("❌ No face detected")
    print("ACTION: Continue scanning...")

# Optional: show results
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detection Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

