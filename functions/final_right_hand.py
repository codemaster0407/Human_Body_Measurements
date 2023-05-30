import bpy
import numpy as np

def find_extreme_points_width(object_name, y_value):
    mesh = bpy.data.objects[object_name].data
    vertices = np.array([v.co for v in mesh.vertices if abs(v.co.y - y_value) <= 0.001])
    # print(vertices)
    leftmost_point = np.min(vertices[:, 0])
    rightmost_point = np.max(vertices[:, 0])
    return leftmost_point, rightmost_point

def find_extreme_points(object_name):
    mesh = bpy.data.objects[object_name].data
    vertices = np.array([v.co for v in mesh.vertices])
    highest_point = np.max(vertices, axis=0)
    lowest_point = np.min(vertices, axis=0)
    return highest_point, lowest_point


## Import the STL file and select the object
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

highest_point, lowest_point = find_extreme_points(object_name)
print("Highest point coordinates:", highest_point)
print("Lowest point coordinates:", lowest_point)
model_height = highest_point[1] - lowest_point[1]
print("Model height:", model_height)




#shoulder line y axis value is being calculated
waistline = highest_point[1] - 0.47*model_height
chestline = highest_point[1] - 0.284*model_height
shoulderline = highest_point[1] - 0.25*model_height
sline = highest_point[1] - 0.22*model_height


print("waistline y-axis value: ",sline)
#print("chestline y-axis value: ",chestline)
#print("shoulderline y-axis value: ",shoulderline)


left_most , right_most = find_extreme_points_width(object_name,sline)
# print("shoulderline y-axis value: ",left_most)


bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.bisect(plane_co=(right_most,19,19), plane_no=(1,0,0), clear_inner=False, clear_outer=True)


#bpy.ops.mesh.bisect(plane_co=(19,19, sline), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)
# Switch to object mode
bpy.ops.object.mode_set(mode='OBJECT')







mesh = obj.data

vertices = np.array([v.co for v in mesh.vertices])
edges = np.array([e.vertices for e in mesh.edges])

circumferences = []

same_plane_pts = {}
z_vals = []

# print(len(vertices))

for i in range(len(vertices)):
    if vertices[i][0] not in z_vals:
        z_vals.append(vertices[i][0])

z_vals = list(set(z_vals))
# print(len(z_vals))

for i in range(len(z_vals)):
    same_plane_pts[z_vals[i]] = []
    

    
for i in range(len(vertices)):
    same_plane_pts[vertices[i][0]].append(np.array(vertices[i]))
    
keys = list(same_plane_pts.keys())

arm_edges = 0
for i in range(len(same_plane_pts)):
    if len(same_plane_pts[keys[i]]) > 50 and keys[i] ==right_most :
        arm_edges = len(same_plane_pts[keys[i]]) 
        print(keys[i])
        
print(arm_edges)


