config = {
    "hostname" :"web1",
    "ip": "192.168.1.10",
    "port": "80"
}

print("The host details are: ")

for key,value in config.items():
    print(f"{key} is {value}")