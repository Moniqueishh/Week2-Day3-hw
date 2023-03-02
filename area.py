# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage


def house():
    l = int(input("What is the length of your house? >> "))
    w = int(input("What is the width of your house? >> "))
    b = (l * w)
    print(f"The sqf of your house is {b}!")

house()