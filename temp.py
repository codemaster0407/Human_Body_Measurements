import os 
import pandas as pd

obj_folder_path = './obj_files'

obj_file_list = sorted(os.listdir(obj_folder_path))
print(obj_file_list)
df = pd.read_excel('./Measurements_file.xlsx')


df['Height (in inches)'] = None


df['obj_path'] = None 

df_sorted = df.sort_values(by='Name')
df_sorted.reset_index(inplace = True)

del df_sorted['index']

# print(df_sorted)


for i in range(len(df_sorted)):
    # print(obj_folder_path+'/' + obj_file_list[i])
    df_sorted['obj_path'][i] = obj_folder_path+'/' + obj_file_list[i]
    
print(df_sorted)

df_sorted.to_csv('annotations.csv')

    
