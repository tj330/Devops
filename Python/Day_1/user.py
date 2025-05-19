from datetime import datetime

name = input("Enter your name: ")
year = int(input("Enter your birth year: "))
age = datetime.now().year - year
print("Hey,", name, ". Your age is:", age)