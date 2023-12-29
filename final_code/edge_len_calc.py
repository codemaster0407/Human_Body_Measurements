import bpy
import numpy as np

import math
import mathutils


def calculate_edge_lengths(mesh, target_y, obj):
    # count = 0 
    
    
    
     
    edge_lengths = []
    for edge in mesh.edges:
        
        vertex1 = obj.matrix_world @ mesh.vertices[edge.vertices[0]].co
        vertex2 = obj.matrix_world @ mesh.vertices[edge.vertices[1]].co
        
        
        y1 = vertex1[2]
        y2 = vertex2[2]
    
        if abs(y1 - target_y) < 0.000001 and abs(y2-target_y) < 0.000001:
            # count+=1
            length = (vertex1 - vertex2).length
            edge_lengths.append(length)
            
    
    total_length = 0
    
    for length in edge_lengths:
        total_length += length
        
    # print(count)
    # print(f'Function output : {total_length}')
    
        
    return total_length