def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"Result: {result:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {result:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
