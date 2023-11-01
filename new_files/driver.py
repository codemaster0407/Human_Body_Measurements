import subprocess
import chest
import waist
import shoulder
import sys
import os
import re
import distance_conversion

import pandas as pd



def split_filename(path):

    temp = list(path.split('\\'))
    
    name = temp[-1]
    
    object_name = list(name.split('.'))
    element = object_name[0]
    return element
    

path_dir = './obj_files/'

obj_file_list = os.listdir('./obj_files')


# shoulder_ms_list = []
# chest_ms_list = []
waist_ms_list = []

actual_height = 69
path = 'obj_files\\anish.obj'

object_name = 'anish'

bm_1 = distance_conversion.convert_to_inches(path, object_name, actual_height)
print(f'Conversion metric from blender to inches is {bm_1}')
waist_measurement = waist.calculate_waist(path, object_name, bm_1)
print(f'Waist measurement in inches is {waist_measurement}')


# print(waist_measurement)

# actual_height = 0

# for file in obj_file_list:
#     path= path_dir + file 
#     object_name = file.split('.')[0]
#     try: 
#         bm1 = distance_conversion.convert_to_inches(path, object_name, actual_height)
#         waist_measurement = waist.calculate_waist(path, object_name, bm1)
#         waist_ms_list.append(waist_measurement) 
#     except: 
#         print('File not found')


# df = pd.read_csv('blender_measurements.csv') 
# df['waist measurement'] = waist_ms_list 


# df.to_csv('blender_measurements.csv')


# names = []
# for file in obj_file_list:
#     path = path_dir + file 
#     object_name = file.split('.')[0]
#     print(path, object_name)
#     names.append(object_name)
    
#     try: 
#         shoulder_measurement = shoulder.calculate_shoulder(path, object_name)
#         # chest_measurement = chest.calculate_chest(path, object_name)
#         # waist_measurement = waist.calculate_waist(path, object_name)
        
     
#         shoulder_ms_list.append(shoulder_measurement)
#         # waist_ms_list.append(waist_measurement)
#         # chest_ms_list.append(chest_measurement)
#     except:
#         print('File not found')

# shoulder_measurement = shoulder.calculate_shoulder('./obj_files/sunil.obj', "sunil")
# print(shoulder_measurement)  

# chest_measurement = chest.calculate_chest('./obj_files/sunil.obj', "sunil")
# print(chest_measurement)

# shoulder_measurement = shoulder.calculate_shoulder('./obj_files/sunil.obj', "sunil")
# print(shoulder_measurement)  
    




