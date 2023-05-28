import bpy
import numpy as np

def find_extreme_points(object_name):
    mesh = bpy.data.objects[object_name].data
    vertices = np.array([v.co for v in mesh.vertices])
    highest_point = np.max(vertices, axis=0)
    lowest_point = np.min(vertices, axis=0)
    return highest_point, lowest_point


## Import the STL file and select the object
filepath = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\model_3.obj"
bpy.ops.import_scene.obj(filepath=filepath)
object_name = "model_3"

obj = bpy.data.objects[object_name]
obj.select_set(True)
bpy.context.view_layer.objects.active = obj


obj = bpy.data.objects[object_name]
obj.select_set(True)
bpy.context.view_layer.objects.active = obj

# Switch to object mode
bpy.ops.object.mode_set(mode='OBJECT')






# Subdivide the mesh
#bpy.ops.object.mode_set(mode='EDIT')
#bpy.ops.mesh.select_all(action='SELECT')
#bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')
#bpy.ops.mesh.select_all(action='SELECT')
#bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')
#bpy.ops.object.mode_set(mode='OBJECT')

# Set the range size for selecting vertices
range_size = 0.0001

highest_point, lowest_point = find_extreme_points(object_name)
print("Highest point coordinates:", highest_point)
print("Lowest point coordinates:", lowest_point)
model_height = highest_point[1] - lowest_point[1]
print("Model height:", model_height)

waistline = highest_point[1] - 0.47*model_height
chestline = highest_point[1] - 0.284*model_height
shoulderline = highest_point[1] - 0.246*model_height
print("waistline y-axis value: ",waistline)
print("chestline y-axis value: ",chestline)
print("shoulderline y-axis value: ",shoulderline)

#bpy.ops.object.mode_set(mode='EDIT')
#bpy.ops.mesh.select_all(action='DESELECT')
#bpy.ops.mesh.bisect(plane_co=(0, waistline, 0), plane_no=(0, 1, 0), clear_inner=True, clear_outer=False)
#bpy.ops.object.mode_set(mode='OBJECT')
#mesh = obj.data



#highest_point, lowest_point = find_extreme_points(object_name)
#print("Highest point coordinates:", highest_point)
#print("Lowest point coordinates:", lowest_point)

bpy.ops.object.mode_set(mode='EDIT')
#bpy.ops.mesh.bisect(plane_co=(19,19,waistline), plane_no=(0,0,1), clear_inner=True, clear_outer=False)
#bpy.ops.mesh.bisect(plane_co=(19,19, chestline), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)
bpy.ops.mesh.bisect(plane_co=(19,19, shoulderline), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)
bpy.ops.object.mode_set(mode='OBJECT')
mesh = obj.data

vertices = np.array([v.co for v in mesh.vertices])
edges = np.array([e.vertices for e in mesh.edges])

circumferences = []

same_plane_pts = {}
z_vals = []

# print(len(vertices))

for i in range(len(vertices)):
    if vertices[i][1] not in z_vals:
        z_vals.append(vertices[i][1])

z_vals = list(set(z_vals))
# print(len(z_vals))

for i in range(len(z_vals)):
    same_plane_pts[z_vals[i]] = []
    

    
for i in range(len(vertices)):
    same_plane_pts[vertices[i][1]].append(np.array(vertices[i]))
    
keys = list(same_plane_pts.keys())

for i in range(len(same_plane_pts)):
    if len(same_plane_pts[keys[i]]) > 200:
        print(len(same_plane_pts[keys[i]]))
        print(keys[i])
        

        
        






# unique_z = []
# for i in range(len(vertices)):
#     unique_z.append(vertices[i][2])

# unique_z = list(sorted(set(unique_z)))

# print(len(unique_z))

# # unique_z = sorted(unique_z)

# plane_points_dict = {}

# for key in unique_z:
#     plane_points_dict[key] = []
    
# for i in range(len(vertices)):
#     if vertices[i][2] in unique_z:
#         plane_points_dict[vertices[i][2]].append(np.array(vertices[i]))
        
# sorted_dict = dict(sorted(plane_points_dict.items()))


# plane_points_keys = list(plane_points_dict.keys())



# # create_aggregated_plots(plane_points_dict, plane_points_keys, "L")
    


# # print(len(unique_z),end = "\n")
# # print(len(vertices))
# prime_key = 0

# for key in plane_points_keys:
#     if len(plane_points_dict[key]) >100:
#         # print(plane_points_keys)
#         prime_key = key
        
# print(prime_key)

# print(len(plane_points_dict[prime_key]))