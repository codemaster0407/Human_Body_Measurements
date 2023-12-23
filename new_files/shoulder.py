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



def calculate_edge_lengths(mesh, target_y, obj):
    count_enter = 0
    counter_outer = 0
    
    
    
    
    edge_lengths = []
    for edge in mesh.edges:
        vertex1 = obj.matrix_world @ mesh.vertices[edge.vertices[0]].co
        vertex2 = obj.matrix_world @ mesh.vertices[edge.vertices[1]].co
        
        
        y1 = vertex1[2]
        y2 = vertex2[2]
        count_outer += 1
        if abs(y1 - target_y) < 0.00001 and abs(y2-target_y) < 0.00001:
            
            count_enter+= 1
            length = (vertex1 - vertex2).length
            edge_lengths.append(length)
            
    
    total_length = 0
    
    for length in edge_lengths:
        total_length += length
        
        
    print(f'Function output : {total_length}')
    # print(counter_enter, count_outer)
        
    return total_length
            
  

  
        
        
        
        


def calculate_shoulder(filepath, object_name, bm_1):
    
    print(filepath, object_name)
    
    bpy.ops.import_scene.obj(filepath=filepath)


    obj = bpy.data.objects.get(object_name)
    
            
      
   
    
        

     
    if obj is not None:
        bpy.context.view_layer.objects.active = obj


        bpy.ops.object.mode_set(mode='OBJECT')
            

        mesh = obj.data
            
        

        height, max_z, min_z = obj_height(mesh)
        
        
        percent_neg = ((0-min_z)/height)
        
        remaining_percentage = 0.758- percent_neg
        
        chest_y = remaining_percentage * height



        
        

        




        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(19,19, chest_y), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

        bpy.ops.object.mode_set(mode='OBJECT')

            
        
  
        
        shoulder_length = calculate_edge_lengths(mesh, chest_y, obj)
        
        
        return shoulder_length * bm_1
        
        


        



path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\chaitanya.obj"
object_name = 'chaitanya'
actual_height = 69

print(calculate_shoulder(path, object_name, actual_height))