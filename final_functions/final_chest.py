import bpy
import numpy as np
import sys

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


### Import the STL file and select the object
# path = sys.argv[1]

def chest_function(path, object_name):
    filepath = path
    bpy.ops.import_scene.obj(filepath=filepath)
    # object_name = obj_name

    obj = bpy.data.objects[object_name]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


    obj = bpy.data.objects[object_name]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Switch to object mode
    bpy.ops.object.mode_set(mode='OBJECT')






    # Subdivide the mesh
    # bpy.ops.object.mode_set(mode='EDIT')
    # bpy.ops.mesh.select_all(action='SELECT')
    # bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')
    # bpy.ops.mesh.select_all(action='SELECT')
    # bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')
    # bpy.ops.object.mode_set(mode='OBJECT')

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




    # Count the number of vertices between the leftmost and rightmost points
    num_vertices = np.sum((vertices[:, 0] > leftmost_point) & (vertices[:, 0] < rightmost_point) & (np.abs(vertices[:, 1] - chestline) <= 0.001))

    # print("Number of vertices between leftmost and rightmost points at chestline:", num_vertices)
    edge_length = 0.1118421052631579
    print('Chest circumference is ', num_vertices * edge_length)

    #original Chest circumference 
    original_chest = 35

    print('error between original and predicted' , original_chest - (num_vertices * edge_length))