import bpy
import numpy as np

import math
import mathutils



def obj_height(mesh):
    num_edges = len(mesh.edges)
    num_vertices = len(mesh.vertices)

    print("Number of Edges:", num_edges)
    print("Number of Vertices:", num_vertices)

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
    
    return max_z - min_z



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
            
            
    

def plane_ver(mesh,target):
    edge_lengths = []
    for vertex in mesh.vertices:
        y  = vertex[2]
        if abs(y - target_y) < 0.001:
            print(vertex)
    
        
        
        
        
        
        


    # Set the file path to your OBJ file
filepath = "C:\\Users\\sumo\\OneDrive\\Desktop\\Deskotp\\4-1 proj\\Human_Body_Measurements\\obj_files\\anish.obj"

    # Import the OBJ file
bpy.ops.import_scene.obj(filepath=filepath)

    # Specify the object name you want to work with
object_name = "anish.027"

   
obj = bpy.data.objects.get(object_name)

    # Check if the object exists
if obj is not None:
    bpy.context.view_layer.objects.active = obj

        # Switch to OBJECT mode (in case you're not already in that mode)
    bpy.ops.object.mode_set(mode='OBJECT')
        
    bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
        
    lowest_point = min(bbox, key=lambda v: v.z)
    translation_vector = mathutils.Vector((0,0,0)) - lowest_point
    obj.location += translation_vector
        
    mesh = obj.data
        
       

    height = obj_height(mesh)



    
    

    chest_y = height - 0.33 * height




    obj = bpy.data.objects.get(object_name)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.bisect(plane_co=(19,19, chest_y), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

    bpy.ops.object.mode_set(mode='OBJECT')
    
    bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
        
    lowest_y = min(bbox, key=lambda v: v.z)
#    print(lowest_y[2])
    
#    print(type(lowest_y))

    
#    print(chest_y, lowest_y[2])
    
    
    calculate_edge_lengths(mesh, lowest_y[2])
    
    
    centroid = obj.location
    
    plane_ver(mesh,lowest_y[2])
    
                

      
        
        

else:
    print(f"Object '{object_name}' not found.")












