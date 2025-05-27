try:
    with open("important_config.txt", "r") as f:
        print("File contents are: ")
        print(f.readlines())

except FileNotFoundError:
    print(f"Config file not found!")

finally:
    print("Operation complete")