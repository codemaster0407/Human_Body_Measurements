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

    # y_leftmost = int(coordinates[2][1] )
    # y_rightmost = int(coordinates[31][1])
    
    z_leftmost = int(coordinates[17][2])
    z_rightmost = int(coordinates[18][2])
    

    # cv2.circle(image, (coordinates[17][0], coordinates[17][1]), radius=5, color=(255, 0, 0), thickness=-1)
    # cv2.circle(image, (coordinates[18][0], coordinates[18][1]), radius=5, color=(255, 0, 0), thickness=-1)
    # cv2.circle(image, (coordinates[2][0], coordinates[2][1]), radius=5, color=(255, 0, 0), thickness=-1)
    # cv2.circle(image, (coordinates[31][0], coordinates[31][1]), radius=5, color=(255, 0, 0), thickness=-1)
    
    plt.imshow(image)
    plt.show()
    


    # print(x_leftmost, y_leftmost, z_leftmost)

    # print(x_rightmost, y_rightmost, z_rightmost)
   

    #Normalize the points based on the left most and the right most points

    normalized_coordinates = []
    for point in coordinates:
        
        x_norm = (point[0]) / (x_max)
        y_norm = (point[1]) / (y_max)
        # x_norm = point[0]
        # y_norm = point[1]
                       

        
        normalized_coordinates.append([round(x_norm,4), round(y_norm,4)])
        
    return normalized_coordinates

def change_path(path):
    changed_path = path.replace('\\', '\\\\')
    return changed_path


if __name__=="__main__":
    # folder_path = 'Photos\\background_remove'


    # file_paths = []

    # # Use os.walk() to traverse the folder and collect file paths
    # for root, directories, files in os.walk(folder_path):
    #     for filename in files:
    #         file_path = os.path.join(root, filename)
    #         # file_path = change_path(file_path)
    #         # print(file_path)
    #         file_paths.append(file_path)
            
    
    
    # # print(file_paths)
    
    # remove_indices = [1, 3, 4, 6, 17,18, 19, 20, 21, 22, 30, 31]

    # model_name = []
    # coordinates_2d = []
    # for path in file_paths:
    #     two_dim_coordinates = normalized_coordinates(path)
    #     filtered_list = [value for index, value in enumerate(two_dim_coordinates) if index not in remove_indices]
    #     # print(filtered_list[0])
    #     model_name.append(list(path.split('\\'))[2].split('.')[0])
    #     coordinates_2d.append(filtered_list)
      
        
        
    # list_model_name = []
    # x_coordinates = []
    # y_coordinates = []
    
    # for index in range(len(coordinates_2d)):
    #     for pt in coordinates_2d[index]:
    #         x_coordinates.append(pt[0])
    #         y_coordinates.append(pt[1])
    #         list_model_name.append(model_name[index])
            
    # data = {
    #     'model_name' : list_model_name, 
    #     'x': x_coordinates, 
    #     'y': y_coordinates
    # }
    
    # df = pd.DataFrame(data)
    # df.to_csv('2d_dataset.csv')
        
    
    
    
    # print(len(coordinates_2d[0]))

 
    path = 'Photos\\background_remove\\prateeth.jpg'
    two_dim = normalized_coordinates(path)
    # print(len(two_dim))
    print(two_dim)



