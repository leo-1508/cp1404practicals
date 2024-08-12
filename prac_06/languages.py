"""
Module: languages
Estimated time: 15 minutes

This module creates instances of ProgrammingLanguage and demonstrates their usage.
"""

from programming_language import ProgrammingLanguage

# Create instances of ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print the details of each language
print(python)
print(ruby)
print(visual_basic)

# Create a list of programming languages
languages = [python, ruby, visual_basic]

# Print the names of all dynamically typed languages
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
