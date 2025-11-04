# Date: Oct 27, 2025
# Name: "Lab3_Alyssa_Lucas.py - Area Calculation App"
# Programmer: Alyssa and Lucas
# Description: Application to calculate areas of Circle, Trapezium, Ellipse, and Rhombus

# imports
from math import pi


#----------------------------
# Shape 1: Circle

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float, bool, complex)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return pi * radius ** 2
# ---------------------------

# ---------------------------

# ---------------------------

test_cases = [
    2,
    2.5,
    -3,
    2 + 5j,
    True,
    "radius",
]

for test in test_cases:
    try:
        print(calculate_circle_area(test))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

#-------------------------

#-------------------------

#-------------------------


#----------------------------
# Shape 2: Trapezium

def calculate_trapezium_area(base, top, height):
    if not all(isinstance(x, (int, float, bool, complex)) for x in [base, top, height]):
        raise TypeError("All dimensions must be numbers")
    if any(x < 0 for x in [base, top, height]):
        raise ValueError("All dimensions must be non-negative")
    return 0.5 * (base + top) * height

# ---------------------------


#----------------------------
# Shape 3: Ellipse

def calculate_ellipse_area(major_axis, minor_axis):
    if not all(isinstance(x, (int, float, bool, complex)) for x in [major_axis, minor_axis]):
        raise TypeError("All dimensions must be numbers")
    if any(x < 0 for x in [major_axis, minor_axis]):
        raise ValueError("All dimensions must be non-negative")
    return pi * major_axis * minor_axis

# ---------------------------


#----------------------------
# Shape 4: Rhombus

def calculate_rhombus_area(diagonal1, diagonal2):
    if not all(isinstance(x, (int, float, bool, complex)) for x in [diagonal1, diagonal2]):
        raise TypeError("All diagonals must be numbers")
    if any(x < 0 for x in [diagonal1, diagonal2]):
        raise ValueError("All diagonals must be non-negative")
    return 0.5 * diagonal1 * diagonal2

#----------------------------

