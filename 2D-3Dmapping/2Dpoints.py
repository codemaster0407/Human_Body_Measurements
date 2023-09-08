import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd

def find_y_min_max(coordinates):
    y_min = 0
    y_max = 0

    y_min = min(coordinates[5][1], coordinates[2][1])
    y_max = max(coordinates[32][1], coordinates[31][1])
    return y_min, y_max

def normalized_coordinates(path, write_to_csv=False, csv_filename=None):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    image_path = path

    image = cv2.imread(image_path)
    size = (480, 640)
    image = cv2.resize(image, size)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    coordinates = []
    image_height, image_width, _ = image.shape

    if results.pose_landmarks:
        for i, landmark in enumerate(results.pose_landmarks.landmark):
            x = int(landmark.x * image_width)
            y = int(landmark.y * image_height)
            z = int(landmark.z * image_width)  # Using image_width for depth

            coordinates.append([i, x, y, z])

            # Annotate the landmark points on the image with numerical labels
            cv2.circle(image, (x, y), radius=5, color=(0, 255, 0), thickness=-1)
            cv2.putText(image, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    x_max = image.shape[1]
    y_max = image.shape[0]
    x_leftmost = int(coordinates[17][0])
    x_rightmost = int(coordinates[18][0])
    y_leftmost, y_rightmost = find_y_min_max(coordinates)
    z_leftmost = int(coordinates[17][3])
    z_rightmost = int(coordinates[18][3])

    cv2.circle(image, (coordinates[17][1], coordinates[17][2]), radius=5, color=(255, 0, 0), thickness=-1)
    cv2.circle(image, (coordinates[18][1], coordinates[18][2]), radius=5, color=(255, 0, 0), thickness=-1)
    cv2.circle(image, (coordinates[2][1], coordinates[2][2]), radius=5, color=(255, 0, 0), thickness=-1)
    cv2.circle(image, (coordinates[31][1], coordinates[31][2]), radius=5, color=(255, 0, 0), thickness=-1)

    plt.imshow(image)
    plt.show()

    data = []
    for i, coord in enumerate(coordinates):
        x_norm = coord[1] / x_max
        y_norm = coord[2] / y_max
        data.append([i, x_norm, y_norm])

        print(f"{i}: [{round(x_norm, 4)}, {round(y_norm, 4)}]")

    if write_to_csv:
        if csv_filename is None:
            csv_filename = 'landmark_coordinates1.csv'
        df = pd.DataFrame(data, columns=['#', 'X', 'Y'])
        df.to_csv(csv_filename, index=False)
        #print(f'Data written to {csv_filename}')

    return data

if __name__ == "__main__":
    path = '/Users/pradhammummaleti/Desktop/Human_Body_Measurements/Photos/background_remove/srinath.jpg'
    two_dim = normalized_coordinates(path, write_to_csv=False)
