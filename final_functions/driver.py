import subprocess

# List of file names to run
file_names = ["final_chest.py", "final_lefthand.py", "final_righthand.py", "final_shoulder.py", "final_waist.py"]


# path = "/path/to/file"

# Create a list to store the subprocesses
processes = []

# Launch subprocesses for each file
for file_name in file_names:
    process = subprocess.Popen(["python", file_name])
    processes.append(process)

# Wait for all subprocesses to finish
for process in processes:
    process.wait()