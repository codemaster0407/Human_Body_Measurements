import subprocess
import final_chest
import wrist
import final_waist 
import final_righthand
import final_shoulder
import final_lefthand 



def split_filename(path):

    temp = list(path.split('\\'))
    
    name = temp[-1]
    
    object_name = list(name.split('.'))
    element = object_name[0]
    return element
    
 
    
    
    
    

path = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\obj_files\\result_anish_256.obj"
object_name = split_filename(path)



final_chest.chest_function(path, object_name)
wrist.wrist_function(path, object_name)
final_waist.waist_function(path, object_name)
final_righthand.right_hand_function(path, object_name)
final_lefthand.left_hand_function(path, object_name)
final_shoulder.shoulder_function(path, object_name)


file_names = ["final_chest.py", "final_lefthand.py", "final_righthand.py", "final_shoulder.py", "final_waist.py", "wrist.py"]
processes = []


for file_name in file_names:
    process = subprocess.Popen(["python", file_name])
    processes.append(process)

for process in processes:
    process.wait()