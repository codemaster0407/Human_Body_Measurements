import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

def list_files():
    import os

    folder_path = '/path/to/folder'  # Replace with the path to your folder

    # Get all file names in the folder
    file_names = os.listdir(folder_path)

    # Print the file names
    for file_name in file_names:
        print(file_name)







def normalized_coordinates(path):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()



    image_path = path
    # image_path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\Photos\\Reddy\\IMG-20230618-WA0015-removebg-preview.png"
    image = cv2.imread(image_path)

  


    # Convert the image to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image
    results = pose.process(image_rgb)


    coordinates = []
    image_height, image_width, _ = image.shape

    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            # Extract the x, y, and z coordinates
            x = landmark.x
            y = landmark.y
            z = landmark.z
            
            # coordinates.append([x,y,z])
            image_height, image_width, depth = image.shape
            x = int(landmark.x * image_width)
            y = int(landmark.y * image_height)
            z = int(landmark.z * depth)
            
            coordinates.append([x,y,z])
            
            
            
            
            # Add a dot at the landmark coordinates
            cv2.circle(image, (x, y), radius=5, color=(0, 255, 0), thickness=-1)







    x_leftmost = int(coordinates[17][0] )
    x_rightmost = int(coordinates[18][0]) 

    y_leftmost = int(coordinates[17][1] )
    y_rightmost = int(coordinates[18][1])
    
    z_leftmost = int(coordinates[17][2])
    z_rightmost = int(coordinates[18][2])
    

    cv2.circle(image, (x_leftmost, y_leftmost), radius=5, color=(255, 0, 0), thickness=-1)
    cv2.circle(image, (x_rightmost, y_rightmost), radius=5, color=(255, 0, 0), thickness=-1)


    print(x_leftmost, y_leftmost, z_leftmost)
    print(x_rightmost, y_rightmost, z_rightmost)
   

    #Normalize the points based on the left most and the right most points

    normalized_coordinates = []
    for point in coordinates:
        
        x_norm = (point[0] -  x_leftmost) / (x_rightmost - x_leftmost)
        y_norm = (point[1] -  y_leftmost) / (y_rightmost - y_leftmost)

        
        normalized_coordinates.append([x_norm, y_norm])
        
    return normalized_coordinates


if __name__ == '__main__':
    path = 
    






