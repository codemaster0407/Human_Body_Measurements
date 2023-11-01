
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





def convert_to_inches(filepath, object_name, actual_height):
   
    bpy.ops.import_scene.obj(filepath=filepath)

    
    obj = bpy.data.objects.get(object_name)

 
    if obj is not None:
        bpy.context.view_layer.objects.active = obj


        bpy.ops.object.mode_set(mode='OBJECT')
            
  
            
        mesh = obj.data
            
        

        height, max_z, min_z = obj_height(mesh)
        
        bm_1 = actual_height / height
        
        return bm_1
        

