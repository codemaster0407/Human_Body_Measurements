import subprocess
file_names = ["final_chest.py", "final_lefthand.py", "final_righthand.py", "final_shoulder.py", "final_waist.py", "wrist.py"]
processes = []
for file_name in file_names:
    process = subprocess.Popen(["python", file_name])
    processes.append(process)

for process in processes:
    process.wait()