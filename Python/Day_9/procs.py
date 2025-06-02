import psutil


for process in psutil.process_iter(['pid', 'name']):
    print(f"Name: {process.info['name']}, PID: {process.info['pid']}")