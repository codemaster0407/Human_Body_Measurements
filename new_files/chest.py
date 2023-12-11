import bpy
import numpy as np

import math
import mathutils



def obj_height(mesh):
    num_edges = len(mesh.edges)
    num_vertices = len(mesh.vertices)


    vertices = np.zeros((len(mesh.vertices), 3))
    for i, vertex in enumerate(mesh.vertices):
        vertices[i] = vertex.co[:]


    edges = np.zeros((len(mesh.edges), 2), dtype=np.float64)
    for i, edge in enumerate(mesh.edges):
        edges[i] = edge.vertices[:]



    min_z = np.min(vertices[:, 1])
    max_z = np.max(vertices[:, 1])
    
    return max_z - min_z, max_z, min_z



def hands_slicing(mesh):
    
    select_vertices = [v for v in mesh.vertices if v.select]

    most_right = 100
    most_left = -100

    for v in select_vertices:
        if(v.co.x > most_left and v.co.x < 0.25):
            most_left = v.co.x
            most_left_idx = v.index
        if(v.co.x < most_right and v.co.x > -0.25):
            most_right = v.co.x
            most_right_idx = v.index
            
            
    
    return most_left-0.03, most_right+0.03



def calculate_edge_lengths(mesh, target_y, obj):
    # print(target_y)
    edge_count = 0
    for edge in mesh.edges:
        vertex1 = obj.matrix_world @ mesh.vertices[edge.vertices[0]].co
        vertex2 = obj.matrix_world @ mesh.vertices[edge.vertices[1]].co
        
        y1 = vertex1[1]
        y2 = vertex2[1]
        
        if y1 == target_y :
            # print('Count of edges')
            edge_count += 1 
            
        break
    
    print(f'Count of edges : {edge_count}')
    
        


def calculate_chest(filepath, object_name, bm_1):
    # print(filepath, object_name)

    
    # print(filepath, object_name)

    bpy.ops.import_scene.obj(filepath=filepath)


    
    obj = bpy.data.objects.get(object_name)

    if obj is not None:
        bpy.context.view_layer.objects.active = obj

    
        bpy.ops.object.mode_set(mode='OBJECT')
            
    
            
        mesh = obj.data
            
        

        height, max_z, min_z = obj_height(mesh)
        
        
        
        #1Blender metric distance real time calculation 
        
        
        
        # print(height)
        percent_neg = ((0-min_z)/height)
        
        
        remaining_percentage = 0.696- percent_neg
        
        chest_y = remaining_percentage * height
        
        
        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(19,19, chest_y), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

        bpy.ops.object.mode_set(mode='OBJECT')
        
        bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
            
        lowest_y = min(bbox, key=lambda v: v.z)
        

        
        chest_length =  calculate_edge_lengths(mesh, chest_y, obj)
        
        # print(chest_length)
        return chest_length * bm_1
    
        
        



path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\anish.obj"
object_name = 'anish'
actual_height = 68
print(calculate_chest(path, object_name, actual_height))







