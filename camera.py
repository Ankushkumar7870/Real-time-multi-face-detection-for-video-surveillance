import cv2
import os
import csv
from datetime import datetime

class VideoCamera:
    def __init__(self):
        # Initialize camera once
        self.cap = cv2.VideoCapture(0)

        # Load face recognizer and labels once
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("recognizer.yml")
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Load labels
        self.labels = {}
        with open("labels.txt") as f:
            for line in f:
                label_id, name = line.strip().split(',')
                self.labels[int(label_id)] = name

        self.logged_names = set()

    def __del__(self):
        # Release camera on object deletion
        self.cap.release()

    def mark_attendance(self, name):
        """ Mark attendance for detected person """
        if name not in self.logged_names:
            self.logged_names.add(name)
            with open("attendance.csv", "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect multiple faces in the frame
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Extract face from the frame (grayscale)
            face = gray[y:y+h, x:x+w]

            # Predict the label for the face
            label_id, confidence = self.recognizer.predict(face)

            if confidence < 60:
                name = self.labels.get(label_id, "Unknown")
                self.mark_attendance(name)
            else:
                name = "Unknown"

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        # Convert to JPEG
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

