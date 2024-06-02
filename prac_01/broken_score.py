"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))
while score >= 0:
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excell  ent")
    elif score >= 50:
        print("Passable")
    else:
        print("bad")
    score = float(input("Enter score: "))