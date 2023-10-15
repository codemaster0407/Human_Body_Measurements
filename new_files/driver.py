import subprocess
import chest
import waist
import shoulder
import sys
import os
import re

import pandas as pd



def split_filename(path):

    temp = list(path.split('\\'))
    
    name = temp[-1]
    
    object_name = list(name.split('.'))
    element = object_name[0]
    return element
    

path_dir = './obj_files/'

obj_file_list = os.listdir('./obj_files')


shoulder_ms_list = []
names = []
for file in obj_file_list:
    path = path_dir + file 
    object_name = file.split('.')[0]
    # print(path, object_name)
    names.append(object_name)
    
    try: 
        shoulder_measurement = shoulder.calculate_shoulder(path, object_name)
        shoulder_ms_list.append(shoulder_measurement)
    except:
        print('File not found')


data = {
    'names': names, 
    'shoulder_measurement': shoulder_ms_list 
}

df = pd.DataFrame(data)
df.to_csv('blender_measurements.csv')




