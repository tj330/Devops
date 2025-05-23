with open("config.ini", "r") as f:
    content = f.readlines()

    for lines in content:
        line = lines.split("=", 1)

        if(len(line) > 1):
            print(f"Port no. is {line[1]}")
