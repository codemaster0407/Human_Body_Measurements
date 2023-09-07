# import nbformat
# from nbconvert import PythonExporter





# import mediapipe as mp
# import cv2
# import matplotlib.pyplot as plt
# import os 
# import pandas as pd





# def find_y_min_max(coordinates):
#     y_min = 0
#     y_max = 0
    

    
#     y_min = min(coordinates[5][1], coordinates[2][1])
#     y_max = max(coordinates[32][1], coordinates[31][1])
#     # print(coordinates[32][1], coordinates[31][1]) 
#     # print(y_max, y_min)
#     return y_min, y_max



# def normalized_coordinates(path):
#     mp_pose = mp.solutions.pose
#     pose = mp_pose.Pose()



#     image_path = path
#     # image_path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\Photos\\Reddy\\IMG-20230618-WA0015-removebg-preview.png"
#     image = cv2.imread(image_path)

  


#     # Convert the image to RGB format
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Process the image
#     results = pose.process(image_rgb)


#     coordinates = []
#     image_height, image_width, _ = image.shape

#     if results.pose_landmarks:
#         for landmark in results.pose_landmarks.landmark:
#             # Extract the x, y, and z coordinates
#             x = landmark.x
#             y = landmark.y
#             z = landmark.z
            
#             # coordinates.append([x,y,z])
#             image_height, image_width, depth = image.shape
#             x = int(landmark.x * image_width)
#             y = int(landmark.y * image_height)
#             z = int(landmark.z * depth)
            
#             coordinates.append([x,y,z])
            
            
            
            
#             # Add a dot at the landmark coordinates
#             cv2.circle(image, (x, y), radius=5, color=(0, 255, 0), thickness=-1)





#     # print(image.shape)
#     x_min = 0
#     y_min = 0
    
#     x_max = image.shape[1]
#     y_max = image.shape[0]

#     x_leftmost = int(coordinates[17][0] )
#     x_rightmost = int(coordinates[18][0]) 
    
#     #For finding the leftmost and right most y's
    
#     y_leftmost, y_rightmost = find_y_min_max(coordinates)

#     # y_leftmost = int(coordinates[2][1] )
#     # y_rightmost = int(coordinates[31][1])
    
#     z_leftmost = int(coordinates[17][2])
#     z_rightmost = int(coordinates[18][2])
    

#     cv2.circle(image, (coordinates[17][0], coordinates[17][1]), radius=5, color=(255, 0, 0), thickness=-1)
#     cv2.circle(image, (coordinates[18][0], coordinates[18][1]), radius=5, color=(255, 0, 0), thickness=-1)
#     cv2.circle(image, (coordinates[2][0], coordinates[2][1]), radius=5, color=(255, 0, 0), thickness=-1)
#     cv2.circle(image, (coordinates[31][0], coordinates[31][1]), radius=5, color=(255, 0, 0), thickness=-1)
    
#     # plt.imshow(image)
#     # plt.show()
    


#     # print(x_leftmost, y_leftmost, z_leftmost)

#     # print(x_rightmost, y_rightmost, z_rightmost)
   

#     #Normalize the points based on the left most and the right most points

#     normalized_coordinates = []
#     for point in coordinates:
        
#         x_norm = (point[0]) / (x_max)
#         y_norm = (point[1]) / (y_max)
#         # x_norm = point[0]
#         # y_norm = point[1]
                       

        
#         normalized_coordinates.append([round(x_norm,4), round(y_norm,4)])
        
#     return normalized_coordinates

# def change_path(path):
#     changed_path = path.replace('\\', '\\\\')
#     return changed_path


# def return_points(image_points):

#     output_notebook_path = 'neural_networks\\model_load.ipynb'
#     output_function_name = 'return_3d'  


#     with open(output_notebook_path, 'r') as nbfile:
#         notebook = nbformat.read(nbfile, as_version=4)


#     code_cells = [cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']


#     for code in code_cells:
#         if output_function_name in code:
#             exec(code)  

#     result = return_3d(image_point)  

#     print("Output from the notebook function:", result)