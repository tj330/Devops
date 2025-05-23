import os.path as p

if (p.isfile("config.ini")):
  print("File exists")
else:
  with open("config.ini", "w") as f:
    f.write("[server]\nport=8080")
    print("Default content written")
