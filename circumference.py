# 2) Has a function to calculate the circumference of a circle

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

import math


def circle():
    r = int(input("What is the radius of the circle? >> "))
    a = (2 * 3.14 * r)
    print(f"The Circumference of the circle is {a}!")


circle()