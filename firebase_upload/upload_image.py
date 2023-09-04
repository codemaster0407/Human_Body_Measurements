# Photos\all_photos

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os

# Initialize Firebase Admin SDK with your credentials
cred = credentials.Certificate('measure-3d-firebase-adminsdk-1k969-e6e979d187.json')
firebase_admin.initialize_app(cred)






# Specify the folder path you want to search
folder_path = 'Photos\\all_photos'

# Initialize an empty list to store file paths
file_paths = []

# Use os.walk() to traverse the folder and collect file paths
for root, directories, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_paths.append(file_path)



bucket_name = 'gs://measure-3d.appspot.com'


# bucket = storage.bucket(bucket_name)


for image_path in file_paths:

    bucket = storage.bucket()

    img_name = list(image_path.split('.'))
    print(img_name)
    # Destination path within Firebase Storage
    
    firebase_url = 'https://console.firebase.google.com/u/1/project/measure-3d/database/measure-3d-default-rtdb/data/~2Fbg_removed'
    destination_path = f'firebase_url/bg_removed/{img_name[0]}' 

    blob = bucket.blob(destination_path)
    blob.upload_from_filename(image_path)
    
    

    print(f"Image uploaded")

