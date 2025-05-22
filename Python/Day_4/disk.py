disks=[40, 70, 90, 55]

for usage in disks:
  if usage < 80:
    print(f"disk usage {usage}% is under threshold")
  else:
    print(f"disk usage {usage}% is over threshold")