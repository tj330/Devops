import sys

if len(sys.argv) != 3:
        print("usage : python3 <this filename> num1 num2")

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

sum = num1 + num2

print(f"Sum is {sum}")