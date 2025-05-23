import os

if (os.path.isfile("temp.txt")):
    os.remove("temp.txt")
    print("Successfully deleted file temp.txt")
else:
    print("File temp.txt does not exist")
