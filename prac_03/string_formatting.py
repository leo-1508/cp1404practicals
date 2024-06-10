"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

year = 1922
model = "Gibson L-5 CES"
price = 16036

formatted_string = f"{year} {model} for about ${price:,.0f}!"
print(formatted_string)

for i in range(11):
    result = 2 ** i
    print(f"2 ^ {i:2} is {result:4}")