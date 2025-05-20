import time

num = 10

print("Countdown begins: ")

while num != 0:
    print(num)
    num -= 1
    time.sleep(1)

print("Blast off!")