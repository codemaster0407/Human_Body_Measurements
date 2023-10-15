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
    
    edge_lengths = []
    
    right_most, left_most = hands_slicing(mesh)

   
    for edge in mesh.edges:
        vertex1 = obj.matrix_world @ mesh.vertices[edge.vertices[0]].co
        vertex2 = obj.matrix_world @ mesh.vertices[edge.vertices[1]].co
        
        
        y1 = vertex1[2]
        y2 = vertex2[2]
        x1 = vertex1[0]
        x2 = vertex2[0]
        
        
        
        if x1 < left_most and x2 < left_most:

            continue
        elif x1 > right_most and x2>right_most:

            continue
     
        
        
        
        
        
        if abs(y1 - target_y) < 0.00001 and abs(y2-target_y) < 0.00001:
                
            
            length = (vertex1 - vertex2).length
            edge_lengths.append(length)
        
            
    
    total_length = 0
    
    for length in edge_lengths:
        total_length += length
        
    return total_length
    

    
        


def calculate_chest(filepath, object_name):


    bpy.ops.import_scene.obj(filepath=filepath)


    
    obj = bpy.data.objects.get(object_name)

    if obj is not None:
        bpy.context.view_layer.objects.active = obj

    
        bpy.ops.object.mode_set(mode='OBJECT')
            
    
            
        mesh = obj.data
            
        

        height, max_z, min_z = obj_height(mesh)
      
        
        percent_neg = ((0-min_z)/height)
        
        
        remaining_percentage = 0.696- percent_neg
        
        chest_y = remaining_percentage * height
        

        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(19,19, chest_y), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

        bpy.ops.object.mode_set(mode='OBJECT')
        
        bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
            
        lowest_y = min(bbox, key=lambda v: v.z)
        

        
        return calculate_edge_lengths(mesh, chest_y, obj)
        
        











