with open("log.txt", "r") as f:
    i = 1
    for lines in f:
        print(i, lines.strip())

        #strip() to remove newline characters

        i += 1
