"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
->A ValueError occurs when the input for the numerator or denominator is not a valid integer
2. When will a ZeroDivisionError occur?
->  A ZeroDivisionError occurs when the denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")