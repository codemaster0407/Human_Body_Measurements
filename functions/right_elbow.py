def right_elbow(path,object_name):   
    if obj is not None:
        bpy.context.view_layer.objects.active = obj

            # Switch to OBJECT mode (in case you're not already in that mode)
        bpy.ops.object.mode_set(mode='OBJECT')
            
        # bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
            
        # lowest_point = min(bbox, key=lambda v: v.z)
        # translation_vector = mathutils.Vector((0,0,0)) - lowest_point
        # obj.location += translation_vector
            
        mesh = obj.data
            
        

        height, max_z, min_z = obj_height(mesh)
        
        # print(height)
        # print(0-min_z)
        
        # print(((0-min_z)/height)*100)
        
        percent_neg = ((0-min_z)/height)
        
        remaining_percentage = 0.75- percent_neg
        
        chest_y = remaining_percentage * height

        obj = bpy.data.objects.get(object_name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(0,-0.15, 0), plane_no=(0, 0, 1), clear_inner=False, clear_outer=False)

        bpy.ops.object.mode_set(mode='OBJECT')
        
        bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
            
        lowest_y = min(bbox, key=lambda v: v.z)
    #    print(lowest_y[2])
        
    #    print(type(lowest_y))

        
    #    print(chest_y, lowest_y[2])
        
        
        calculate_edge_lengths(mesh, lowest_y[2])


    else:
        print(f"Object '{object_name}' not found.")

    select_vertices = [v for v in obj.data.vertices if v.select]

    most_right = 100
    most_left = -100

    for v in select_vertices:
        if(v.co.x > most_left and v.co.x < 0.25):
            most_left = v.co.x
            most_left_idx = v.index
        if(v.co.x < most_right and v.co.x > -0.25):
            most_right = v.co.x
            most_right_idx = v.index
            
    print("left and right: ",most_left,most_right)
    print("indexes of the above: ",most_left_idx,most_right_idx)


    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.mode_set(mode='EDIT')
    ##For right hand bisection
    elbow_height = 0.1843
    bpy.ops.mesh.bisect(plane_co=(-0.2,0,0), plane_no=(1, 0, 0), clear_inner=False, clear_outer=True)

    bpy.ops.mesh.select_all(action = "SELECT")

    bpy.ops.mesh.bisect(plane_co=(0,0,0.05), plane_no=(0.45, 0, 1), clear_inner=False, clear_outer=True)
    #bpy.ops.object.mode_set(mode='OBJECT')

    #sum = 0
    #obj=bpy.context.object
    #if obj.mode == 'EDIT':
    #    bm=bmesh.from_edit_mesh(obj.data)
    #    for v in bm.verts:
    #        if v.select:
    #            sum = sum + 1
    #    print(sum)
    #else:
    #    print("Object is not in edit mode.")