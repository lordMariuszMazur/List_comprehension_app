# Functions practice

# dir() # should displays all available functions(no in VSC, yes in IDLE)


def ping():
    return "Ping!"


x = ping()
print(x)

# Function to return the volume of a sphere. V=4/3*pi*r^3
import math

# For complex numbers, use 'cmath' module
math.pi  # displays pi value


def volume(r):
    "Returns the volume of a sphere with radius r."
    v = (4.0 / 3.0) * math.pi * r**3
    return v


p = volume(2)  # sholud be volume(2) only but it's not working in VSC, ok in IDLE
print(p)

# Keyword Arguments (argument = 0)
# 1 inch=2.54 cm and 1 foot = 12 inches


def cm(feet=0, inches=0):
    "Converts a length from feet and inches to centimeters."
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


q = cm(feet=5)  # in IDLE only cm(feet=5)
print(q)

w = cm(inches=70)  # IDLE only cm(inches=70)
print(w)

e = cm(feet=5, inches=8)  # or cm(inches=8, feet=5) is possible, same result
print(e)

# Important message:
# first non-default (required) argument then default (keyword), so:
# def g(y,x=0) is correct, def g(x=0,y) is incorrect
