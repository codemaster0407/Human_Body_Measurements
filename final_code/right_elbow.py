import bpy
import numpy as np

import math



from edge_len_calc import calculate_edge_lengths
from mesh_height import obj_height       
 

  
        
        
        
        


def calculate_shoulder(filepath, original_height):
    
  
    
    bpy.ops.import_scene.obj(filepath=filepath)

    object_name = bpy.context.selected_objects[0].name
    obj = bpy.data.objects.get(object_name)
    
    
            
      
   
    
        

     
    if obj is not None:
        bpy.context.view_layer.objects.active = obj


        bpy.ops.object.mode_set(mode='OBJECT')
            

        mesh = obj.data
        height, max_z, min_z = obj_height(mesh)
        # print(min_z)
       
        percent_neg = ((0-min_z)/height)
        
        # print(height)
        
        remaining_percentage = 0.595- percent_neg
        
        wrist_y = remaining_percentage * height
        
       



        
        

        
        # wrist_y = 0.05

        # height, max_z, min_z = obj_height(mesh)

        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(19,19,wrist_y), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)
        
#        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.select_all(action = "SELECT")
        bpy.ops.mesh.bisect(plane_co=(-0.2,0,0), plane_no=(1, 0, 0), clear_inner=False, clear_outer=True)

        bpy.ops.object.mode_set(mode='OBJECT')
        
        wrist_length = calculate_edge_lengths(mesh, wrist_y, obj)
        
        
        one_metric = original_height / height
       
        return wrist_length * one_metric

            
        
  

        


        



path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\sreevaatsav.obj"
# object_name = 'sreevaatsav'
actual_height = 69

print(calculate_shoulder(path, actual_height))