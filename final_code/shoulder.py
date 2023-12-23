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
        
        
        percent_neg = ((0-min_z)/height)
        
        remaining_percentage = 0.758- percent_neg
        
        chest_y = remaining_percentage * height



        
        

        




        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(19,19, chest_y), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

        bpy.ops.object.mode_set(mode='OBJECT')

            
        
  
        
        shoulder_length = calculate_edge_lengths(mesh, chest_y, obj)
        
        
        one_metric = original_height / height
        
        
        return shoulder_length * one_metric
        
        


        



path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\chaitanya.obj"
object_name = 'chaitanya'
actual_height = 69

print(calculate_shoulder(path, actual_height))