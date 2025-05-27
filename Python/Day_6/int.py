try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"{a}/{b} is {a/b}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Inputs should be integer")
except Exception as e:
    print(f"An error occured: {e}")