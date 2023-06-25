import bpy
import numpy as np
# import sys
import anchor_points 

def find_extreme_points(object_name):
    mesh = bpy.data.objects[object_name].data
    vertices = np.array([v.co for v in mesh.vertices])
    highest_point = np.max(vertices, axis=0)
    lowest_point = np.min(vertices, axis=0)
    return highest_point, lowest_point

def find_extreme_points_width(object_name, y_value):
    mesh = bpy.data.objects[object_name].data
    vertices = np.array([v.co for v in mesh.vertices if abs(v.co.y - y_value) <= 0.001])
    leftmost_point = np.min(vertices[:, 0])
    rightmost_point = np.max(vertices[:, 0])
    return leftmost_point, rightmost_point

def find_left_and_rightmost_points(obj_file_path):
    min_x, min_y, min_z = float('inf'), float('inf'), float('inf')
    max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')
    

    with open(obj_file_path, 'r') as obj_file:
        for line in obj_file:
            line = line.strip()
            if line.startswith('v '):
                # Extract vertex coordinates
                vertex = line.split()[1:]
                x = float(vertex[0])
                y = float(vertex[1])
                z = float(vertex[2])
                
                # Update minimum and maximum x-values
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y) 
                min_z = min(min_z, z)
                max_z = max(max_z, z)
                

    return min_x, max_x, min_y, max_y, min_z, max_z



    

def chest_function(path, object_name, image_path):
    filepath = path
    normalized_coordinates = anchor_points.normalized_coordinates(image_path)
    
    
    
    
    
    
    
    
    bpy.ops.import_scene.obj(filepath=filepath)
    # object_name = obj_name
    
    
    

    
    
    min_x, max_x, min_y, max_y, min_z, max_z = find_left_and_rightmost_points(filepath)
    
    print(max_x, max_y, max_z)
    print(min_x, min_y, min_z) 
    
    
    
    
    obj = bpy.data.objects[object_name]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


    obj = bpy.data.objects[object_name]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Switch to object mode
    bpy.ops.object.mode_set(mode='OBJECT')






    

    # Set the range size for selecting vertices
    range_size = 0.0001

    highest_point, lowest_point = find_extreme_points(object_name)
    # print("Highest point coordinates:", highest_point)
    # print("Lowest point coordinates:", lowest_point)
    model_height = highest_point[1] - lowest_point[1]






    # print("Model height:", model_height)

    waistline = highest_point[1] - 0.47*model_height
    chestline = highest_point[1] - 0.3*model_height
    shoulderline = highest_point[1] - 0.246*model_height
    sline = highest_point[1] - 0.22*model_height


    # print("waistline y-axis value: ",waistline)
    # print("chestline y-axis value: ",chestline)
    # print("shoulderline y-axis value: ",shoulderline)

    bpy.ops.object.mode_set(mode='EDIT')




    bpy.ops.mesh.bisect(plane_co=(19,19, chestline), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

    bpy.ops.object.mode_set(mode='OBJECT')
    mesh = obj.data

    vertices = np.array([v.co for v in mesh.vertices])
    edges = np.array([e.vertices for e in mesh.edges])

    bpy.ops.object.mode_set(mode='OBJECT')
    mesh = obj.data

    vertices = np.array([v.co for v in mesh.vertices])
    edges = np.array([e.vertices for e in mesh.edges])
    leftmost_point, rightmost_point = find_extreme_points_width(object_name, sline)
    
    
    temp_vertices = []
    for vertex in vertices: 
        if(np.abs(vertex[1] - chestline) <= 0.001):
            temp_vertices.append(vertex) 
            
            

            
     
     
     
    # normalized_vertices = []        
    # for vertex in temp_vertices:
    #     x = (vertex[0] - min_x) / (max_x - min_x)  
    #     y = (vertex[1] - min_y) / (max_y - min_y)  
    #     z = (vertex[2] - min_z) / (max_z - min_z)  
    #     normalized_vertices.append([x,y,z]) 
    
    print(normalized_coordinates[13], normalized_coordinates[14])
    
    left_elbow_x = normalized_coordinates[13][0] * (max_x - min_x) + min_x
    left_elbow_y = normalized_coordinates[13][1] * (max_y + min_y) - min_y 
    
    print(temp_vertices[0][1])
    print('denorm' , left_elbow_y) 
        
    
    
    
        
    
    
    
    
            
    
            
        




    # Count the number of vertices between the leftmost and rightmost points
    num_vertices = np.sum((vertices[:, 0] > leftmost_point) & (vertices[:, 0] < rightmost_point) & (np.abs(vertices[:, 1] - chestline) <= 0.001))

    # print("Number of vertices between leftmost and rightmost points at chestline:", num_vertices)
    edge_length = 0.1118421052631579
    print('Chest circumference is ', num_vertices * edge_length)

    #original Chest circumference 
    original_chest = 35

    print('error between original and predicted' , original_chest - (num_vertices * edge_length))
    
    
    
    
if __name__ == '__main__':
    chest_function("C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\reddy.obj", "reddy", "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\Photos\\Reddy\\IMG-20230618-WA0015-removebg-preview.png")