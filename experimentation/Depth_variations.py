import bpy

# Set the viewport to front view
bpy.ops.view3d.viewnumpad(type='FRONT')

# Get the active object (assuming it's the 3D model you want to measure)
obj = bpy.context.active_object

# Create an empty list to store the depths
depths = []

# Loop through all vertices of the object
for vertex in obj.data.vertices:
    # Transform the vertex coordinates from object space to world space
    world_coords = obj.matrix_world @ vertex.co
    
    # Append the z-coordinate (depth) to the list
    depths.append(world_coords.z)

# Sort the depths
depths.sort()

# Print the sorted depths
print("Depths along the z-axis from front view:")
for depth in depths:
    print(depth)
import bpy

# Assuming you have a specific vertex you want to access (replace [0] with the desired index)
vertex = bpy.context.object.data.vertices[0]

# Print the z-coordinate of the vertex
print("Z-Coordinate of the Vertex:", vertex.co.z)
