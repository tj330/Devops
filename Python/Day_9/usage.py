import psutil

disk_usage = psutil.disk_usage('/')
# since 1024³ bytes = 1GB
print(f"Total disk space: {disk_usage.total / (1024**3):.2f} GB")
print(f"Used disk space: {disk_usage.used / (1024**3):.2f} GB")
print(f"Free disk space: {disk_usage.free / (1024**3):.2f} GB")
print(f"Disk usage: {disk_usage.percent}%")