import subprocess

processes = subprocess.run(["ps", "aux"], capture_output=True, text=True)

services = ["nginx", "python", "mysqld"]

for service in services:
    if service in processes.stdout:
        print(f"{service} is running")
    else:
        print(f"{service} is not running")
