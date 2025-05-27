import os

try:
    os.remove("/test")

except PermissionError:
    print("You did not have necessary permission to delete")

except FileNotFoundError:
    print("File Not Found")

except OSError:
    print("OS Error")