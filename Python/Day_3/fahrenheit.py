def celToFahren(cel):
    fahren = (cel * 9/5) + 32
    return fahren

def main():
    cel = int(input("Enter the temperature in Celsius: "))
    fahren = celToFahren(cel)
    print(f"{cel}°C is equal to {fahren}°F")

if __name__ == "__main__":
    main()