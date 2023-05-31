import bpy
import numpy as np

def find_extreme_points(object_name):
    mesh = bpy.data.objects[object_name].data
    vertices = np.array([v.co for v in mesh.vertices])
    highest_point = np.max(vertices, axis=0)
    lowest_point = np.min(vertices, axis=0)
    return highest_point, lowest_point


### Import the STL file and select the object
filepath = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\pup.obj"
bpy.ops.import_scene.obj(filepath=filepath)
object_name = "pup"

obj = bpy.data.objects[object_name]
obj.select_set(True)
bpy.context.view_layer.objects.active = obj


obj = bpy.data.objects[object_name]
obj.select_set(True)
bpy.context.view_layer.objects.active = obj

# Switch to object mode
bpy.ops.object.mode_set(mode='OBJECT')






# Set the range size for selecting vertices
range_size = 0.0001

highest_point, lowest_point = find_extreme_points(object_name)
# print("Highest point coordinates:", highest_point)
# print("Lowest point coordinates:", lowest_point)
model_height = highest_point[1] - lowest_point[1]



# print(model_height)



# print("Model height:", model_height)

waistline = highest_point[1] - 0.47*model_height
chestline = highest_point[1] - 0.284*model_height
shoulderline = highest_point[1] - 0.246*model_height



# print("waistline y-axis value: ",waistline)
# print("chestline y-axis value: ",chestline)
# print("shoulderline y-axis value: ",shoulderline)

bpy.ops.object.mode_set(mode='EDIT')




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

chest_edges = 0

for i in range(len(same_plane_pts)):
    if len(same_plane_pts[keys[i]]) > 300 :
        shoulder_edges = len(same_plane_pts[keys[i]])
        # print(len(same_plane_pts[keys[i]]))
        # print(keys[i])
        
        

edge_length = 0.1118421052631579
print('The circumference of the shoulder is ', shoulder_edges * edge_length) 

original_shoulder = 41.2

print('error between original and predicted' , original_shoulder - (shoulder_edges * edge_length))



        







        





