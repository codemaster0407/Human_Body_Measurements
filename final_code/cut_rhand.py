import bpy
import numpy as np

import math
import mathutils



import bpy
import numpy as np



def obj_height(mesh):
    num_edges = len(mesh.edges)
    num_vertices = len(mesh.vertices)

    # print("Number of Edges:", num_edges)
    # print("Number of Vertices:", num_vertices)

    # Store the coordinates of vertices in a NumPy array
    vertices = np.zeros((len(mesh.vertices), 3))
    for i, vertex in enumerate(mesh.vertices):
        vertices[i] = vertex.co[:]

    # Store the coordinates of edges in a NumPy array
    edges = np.zeros((len(mesh.edges), 2), dtype=np.float64)
    for i, edge in enumerate(mesh.edges):
        edges[i] = edge.vertices[:]



    min_z = np.min(vertices[:, 1])
    max_z = np.max(vertices[:, 1])
    
    return max_z - min_z, max_z, min_z



def calculate_edge_lengths(mesh, target_y):
    
    edge_lengths = []
    for edge in mesh.edges:
        vertex1 = obj.matrix_world @ mesh.vertices[edge.vertices[0]].co
        vertex2 = obj.matrix_world @ mesh.vertices[edge.vertices[1]].co
        
        
        y1 = vertex1[2]
        y2 = vertex2[2]
        
        if abs(y1 - target_y) < 0.001 and abs(y2-target_y) < 0.001:
            
            print(vertex1[2], target_y, vertex2[2])
            length = (vertex1 - vertex2).length
            edge_lengths.append(length)
            
    
    total_length = 0
    
    for length in edge_lengths:
        total_length += length
        
    print(total_length)
        

def hands(path):

    # Import the OBJ file
    bpy.ops.import_scene.obj(filepath=path)
    object_name = bpy.context.selected_objects[0].name
    obj = bpy.data.objects.get(object_name)
    

    # Check if the object exists
    if obj is not None:
        bpy.context.view_layer.objects.active = obj

        # Switch to OBJECT mode (in case you're not already in that mode)
        bpy.ops.object.mode_set(mode='OBJECT')
            
     
            
        mesh = obj.data
        height, max_z, min_z = obj_height(mesh)
        
        # print(height)
        # print(0-min_z)
        
        # print(((0-min_z)/height)*100)
        
        percent_neg = ((0-min_z)/height)
        remaining_percentage = 0.75- percent_neg
        chest_y = remaining_percentage * height

        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(0,-0.15, 0), plane_no=(0, 0, 1), clear_inner=False, clear_outer=False)

        bpy.ops.object.mode_set(mode='OBJECT')
        
        bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
            
        lowest_y = min(bbox, key=lambda v: v.z)


    else:
        print(f"Object '{object_name}' not found.")

    select_vertices = [v for v in obj.data.vertices if v.select]


    most_right = 100
    most_left = -100

    for v in select_vertices:
        if(v.co.x > most_left and v.co.x < 0.25):
            most_left = v.co.x
            most_left_idx = v.index
        if(v.co.x < most_right and v.co.x > -0.25):
            most_right = v.co.x
            most_right_idx = v.index
            
#    print("left and right: ",most_left,most_right)
#    print("indexes of the above: ",most_left_idx,most_right_idx)


    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.mode_set(mode='EDIT')

    #For right hand bisection
    bpy.ops.mesh.bisect(plane_co=(most_right,0,chest_y), plane_no=(1, 0, 0), clear_inner=True, clear_outer=False)
    bpy.ops.mesh.fill()
    bpy.ops.object.mode_set(mode='OBJECT')


    temppath = 'C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\runtime_folder\\temp.obj'
    obj = bpy.context.active_object
    bpy.ops.export_scene.obj(filepath=temppath, use_selection=True, use_materials=False)
    
    
    bpy.ops.import_scene.obj(filepath=temppath)
    object_name = bpy.context.selected_objects[0].name
    obj1 = bpy.data.objects.get(object_name)
    bpy.context.view_layer.objects.active = bpy.context.scene.objects[object_name]
    # obj1 = bpy.context.active_object
    bpy.ops.object.mode_set(mode='EDIT')


    #For left hand bisection
    bpy.ops.mesh.bisect(plane_co=(most_left,0,chest_y), plane_no=(1, 0, 0), clear_inner=False, clear_outer=True)
    bpy.ops.mesh.fill()

    bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.export_scene.obj(filepath=temppath, use_selection=True, use_materials=False)
    print('EXPORT DONE')
