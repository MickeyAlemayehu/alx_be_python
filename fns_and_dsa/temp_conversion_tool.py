FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if unit == "C":
        f = convert_to_fahrenheit(temp)
        print(f"{temp}\u00B0C is {f:.2f}\u00B0F")
    elif unit == "F":
        c = convert_to_celsius(temp)
        print(f"{temp}\u00B0F is {c:.2f}\u00B0C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
