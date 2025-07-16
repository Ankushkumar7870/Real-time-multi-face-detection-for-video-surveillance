import cv2
import numpy as np
import os

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, labels = [], []
    label_dict = {}
    label_id = 0

    for filename in os.listdir('faces'):
        if filename.endswith('.jpg'):
            path = os.path.join('faces', filename)
            name = filename.split('_')[0]

            if name not in label_dict:
                label_dict[name] = label_id
                label_id += 1

            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            labels.append(label_dict[name])

    recognizer.train(faces, np.array(labels))
    recognizer.write('recognizer.yml')

    with open("labels.txt", "w") as f:
        for name, lid in label_dict.items():
            f.write(f"{lid},{name}\n")

if __name__ == "__main__":
    train()
