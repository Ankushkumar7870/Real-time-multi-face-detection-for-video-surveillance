# 🎥 Real-Time Attendance System 🧑‍🏫
Welcome to the Real-Time Attendance System powered by Facial Recognition! This project utilizes modern face recognition technology to automate attendance tracking in real-time. With a combination of Python, OpenCV, and machine learning, this system captures faces, trains a model, and identifies individuals in live video, all while logging attendance in a CSV file.

🚀 Project Overview
This system works by:

Capturing Faces: First, we register faces by capturing images of individuals using a camera.

Training the Model: Next, a machine learning model is trained using these images to recognize faces.

Real-Time Recognition: Once trained, the model is deployed to recognize faces in a live video feed, identifying individuals as they appear in front of the camera.

Attendance Logging: As faces are recognized, their names are displayed on the video feed, and attendance is automatically logged with timestamps in a CSV file.

🔧 Project Structure
Here's a quick look at the core components of the project:

1. register_faces.py
Captures multiple images of a person’s face for training.

Stores these images in a folder to be used for face recognition training.

2. train_model.py
Trains the facial recognition model using the registered images.

Saves the trained model for real-time face recognition.

3. app.py
The main application that runs the live camera feed and recognizes faces.

Displays the name of the recognized individual above their face on the video feed.

Tracks attendance by adding the person’s name and timestamp to the attendance.csv file.

4. camera.py
Interacts with the camera, running continuous operations for face detection and recognition.

Ensures the system works in real-time, performing all recognition and logging tasks.

5. attendance.csv
Stores attendance data, including the name of the recognized individual and the timestamp of their appearance.

Acts as the log for all attendance records.

📦 Dependencies
To get the system up and running, you’ll need the following Python libraries:

OpenCV (cv2): For image and video processing.

OS: To interact with the file system.

CSV: For reading and writing attendance data.

Datetime: To handle timestamps.

Time: For timing operations.

NumPy: For numerical operations and data handling.

Installation:
To install the required dependencies, use pip:

pip install opencv-python numpy
📝 How to Use
The system runs in four easy steps:

1. Register Faces
Run the register_faces.py script to capture images of the individuals you want to register.

This will save the images, which will be used to train the recognition model.

python register_faces.py

2. Train the Model
Once you’ve captured the images, run the train_model.py script to train the facial recognition model. This model will be able to identify individuals based on the captured data.

python train_model.py

3. Run the Application
After training, run app.py to launch the application. The system will use the camera to detect and identify faces in real-time. The recognized person’s name will appear above their face, and the system will log their attendance.

python app.py

4. Activate the Camera
The camera.py file will continuously monitor the camera feed, trigger face detection, and update the attendance record automatically.

python camera.py

This needs to run only in the condition when we made any changes in our camera.py file and this needs to run only once until and unless we make any changes in camera.py file

5. Attendance Logs
The system logs attendance data in the attendance.csv file. You can open this file to view who attended and when.

💡 How It Works
Face Registration:
When you run the register_faces.py, the system captures multiple images of each individual, ensuring a variety of angles and expressions for better model accuracy.

Model Training:
The images are then used to train the face recognition model. Using the train_model.py script, the model learns to associate the unique features of each face with a name.

Real-Time Recognition:
As you run app.py, the system starts the camera and uses the trained model to detect faces in real-time. When a face is recognized, the person's name is displayed above their face on the screen.

Attendance Tracking:
Every time a person is recognized, their name and the current timestamp are logged into the attendance.csv file. This keeps an up-to-date record of who attended and when.

📊 Example Output
Here’s what the system does:

Video Feed: Displays the live camera stream.

Name Display: Shows the name of the recognized individual above their face.

Attendance Log: Automatically adds an entry to the attendance.csv file.

Example of attendance.csv:

Name	Timestamp
John Doe	2025-04-25 10:15:45
Jane Smith	2025-04-25 10:16:22
John Doe	2025-04-25 10:17:10
🚀 Future Enhancements
Improved Recognition: Use advanced techniques like deep learning to improve accuracy under various conditions (e.g., lighting, face angles).

Face Mask Detection: Add an additional layer of validation to ensure proper attendance tracking during the pandemic.

Graphical User Interface (GUI): Build a user-friendly interface for easier interaction.

//Cloud Storage: Store attendance logs on the cloud for easier access and management.(This will be modified into it in upcomming version of this file.)

📄 License
This project is licensed under the MIT License.

Feel free to modify and extend this system to meet your needs. If you have any questions or suggestions, don’t hesitate to open an issue or submit a pull request!

✨ Enjoy using the Real-Time Attendance System! ✨
