# Dictionary of color names and their hexadecimal codes
COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

(COLOR_TO_HEX)


color_name = input("Enter color name: ").capitalize()
while color_name != "":
    try:
        print(color_name, "is", COLOR_TO_HEX[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").capitalize()


print("Goodbye!")
