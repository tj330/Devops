import os

try:
    os.rmdir("./test")
    print("Successfully removed directory: test")
except Exception as e:
    print(f"An error occured: {e}")