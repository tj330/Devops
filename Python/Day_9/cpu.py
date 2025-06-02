import psutil

# time interval - 1s
usage = psutil.cpu_percent(1)

print(f"CPU usage percentage for the last 1 second is: {usage}%")