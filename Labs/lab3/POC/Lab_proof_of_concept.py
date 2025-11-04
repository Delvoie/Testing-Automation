# Date: Oct 20, 2025
# Name: "App for claculating area of shapes Lab3"
# Programmer: Alyssa and Lucas
# Description: 

# imports 
from math import pi

#----------------------------
# Shape 1: CIRCLE

radii = [2, 0, -3, 2 + 5j, True, "radius", 1 + 2.5]

def circle_area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius must be a positive number")
    return pi * (r ** 2)
    
circle_area_message = "Area of circle with radius = {radius:.2f} is {area:.2f}"

for radius in radii:
    try:
        C_A = circle_area(radius)
        print(circle_area_message.format(radius=radius, area=C_A))
    except (TypeError, ValueError) as e:
        print(f"Error for radius {radius}: {e}")
# ---------------------------

