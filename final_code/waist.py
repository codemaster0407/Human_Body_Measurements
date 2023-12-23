import bpy
import numpy as np
from cut_rhand import hands
import math
import mathutils
import os

from edge_len_calc import  calculate_edge_lengths
from mesh_height import obj_height


    
    
    
        


def calculate_chest(filepath, original_height):
    
    hands(filepath)
    
    if os.listdir('C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\runtime_folder') == []:
        print('Hands cutting is not done')
    else:
        filepath ='C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\runtime_folder\\temp.obj'
        
        
    
    bpy.ops.import_scene.obj(filepath=filepath)
    object_name = bpy.context.selected_objects[0].name


    
    obj = bpy.data.objects.get(object_name)

    if obj is not None:
        bpy.context.view_layer.objects.active = obj

    
        bpy.ops.object.mode_set(mode='OBJECT')
            
    
            
        mesh = obj.data
            
        

        height, max_z, min_z = obj_height(mesh)
        
        
        
        #1Blender metric distance real time calculation 
        
        
        
        # print(height)
        percent_neg = ((0-min_z)/height)
        
        
        remaining_percentage = 0.5- percent_neg
        
        chest_y = remaining_percentage * height
        
        
        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(19,19, chest_y), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

        bpy.ops.object.mode_set(mode='OBJECT')
        
        bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
            
        lowest_y = min(bbox, key=lambda v: v.z)
        

        
        waist_length =  calculate_edge_lengths(mesh, chest_y, obj)
        
       
        
        one_metric = original_height / height
        
        os.remove(filepath)
        
        
        return waist_length * one_metric
    
        
        

# path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\chaitanya.obj"
# # object_name = 'chaitanya'
# actual_height = 69

# print(calculate_chest(path, actual_height))









