def change_path(path):
    changed_path = path.replace('\\', '\\\\')
    return changed_path
# API_KEY = pmhi5tkHFxYshpg2Phz8CvaM


import os
import matplotlib.pyplot as plt
import requests
import time


folder_path = 'Photos\\all_photos'

# Initialize an empty list to store file paths
file_paths = []

# Use os.walk() to traverse the folder and collect file paths
for root, directories, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_path = change_path(file_path)
        # print(file_path)
        file_paths.append(file_path)



api_key = 'pmhi5tkHFxYshpg2Phz8CvaM'





# for img_path in file_paths:
#     # print(img_path)
    
#     img_name = list(img_path.split('\\'))[4]
#     print(img_name)

#     response = requests.post(
# 		'https://api.remove.bg/v1.0/removebg',
# 		files={'image_file': open(img_path, 'rb')},
# 		data={'size': 'auto'},
# 		headers={'X-Api-Key': api_key},
# 	)
#     output_path = f'Photos\\background_remove\\'+ str(img_name)
    
#     print(output_path)
#     if response.status_code == requests.codes.ok:
#         with open(output_path, 'wb') as out:
#             out.write(response.content)
#     else:
#         print("Error:", response.status_code, response.text)
        
#     time.sleep(2)



img_path = 'Photos\\all_photos\\pints.jpg'
response = requests.post(
	'https://api.remove.bg/v1.0/removebg',
	files={'image_file': open(img_path, 'rb')},		
    data={'size': 'auto'},
	headers={'X-Api-Key': api_key},
	)
output_path = f'Photos\\background_remove\\'+ 'pints.jpg'
    
# print(output_path)
if response.status_code == requests.codes.ok:
    with open(output_path, 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
        
	