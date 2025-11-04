# Date: Oct 20, 2025
# Name: "App for claculating area of shapes Lab3"
# Programmer: Alyssa and Lucas
# Description: 

# imports 
from math import pi

#----------------------------
# Shape 1: CIRCLE

radii = [2, 3, "test", -1, 4.5, 1000000]

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


#----------------------------
# Shape 2: Trapezium

trapezium_sides = {
    "Trapezium_base" :   [2, 3, "test", -1, 4.5, 1000000],
    "Trapezium_roof" :   [2, 3, "test", -1, 4.5, 1000000],
    "Trapezium_height" : [2, 3, "test", -1, 4.5, 1000000]
}

def trapezium_area(Trapezium_base, Trapezium_roof, Trapezium_height):
    if not isinstance(Trapezium_base, (int, float)):
        raise TypeError("Base must be a number")
    if Trapezium_base < 0:
        raise ValueError("Base must be a positive number")
    if not isinstance(Trapezium_roof, (int, float)):
        raise TypeError("Roof must be a number")
    if Trapezium_roof < 0:
        raise ValueError("Roof must be a positive number")
    if not isinstance(Trapezium_height, (int, float)):
        raise TypeError("Height must be a number")
    if Trapezium_height < 0:
        raise ValueError("Height must be a positive number")
    return ((Trapezium_roof + Trapezium_base) / 2) * Trapezium_height

trapezium_area_message = "Area of trapeziums with base = {Trapezium_base:.2f}, roof = {Trapezium_roof:.2f}, height = {Trapezium_height:.2f} is {area:.2f}"

for base, roof, height in zip(trapezium_sides["Trapezium_base"], trapezium_sides["Trapezium_roof"], trapezium_sides["Trapezium_height"]):
    try:
        T_A = trapezium_area(base, roof, height)
        print(trapezium_area_message.format(Trapezium_base=base, Trapezium_roof=roof, Trapezium_height=height, area=T_A))
    except (TypeError, ValueError) as e:
        print(f"Error for trapezium with base {base}, roof {roof}, height {height}: {e}")
# ---------------------------



#----------------------------
# Shape 3: Ellipse

ellipse_dimensions = {
    "Ellipse_major_axis" : [2, 3, "test", -1, 4.5, 1000000],
    "Ellipse_minor_axis" : [2, 3, "test", -1, 4.5, 1000000]
}

def ellipse_area(Ellipse_major_axis, Ellipse_minor_axis):
    if not isinstance(Ellipse_major_axis, (int, float)):
        raise TypeError("Major axis must be a number")
    if Ellipse_major_axis < 0:
        raise ValueError("Major axis must be a positive number")
    if not isinstance(Ellipse_minor_axis, (int, float)):
        raise TypeError("Minor axis must be a number")
    if Ellipse_minor_axis < 0:
        raise ValueError("Minor axis must be a positive number")
    return pi * Ellipse_major_axis * Ellipse_minor_axis

ellipse_area_message = "Area of ellipses with major axis = {Ellipse_major_axis:.2f}, minor axis = {Ellipse_minor_axis:.2f} is {area:.2f}"

for major_axis, minor_axis in zip(ellipse_dimensions["Ellipse_major_axis"], ellipse_dimensions["Ellipse_minor_axis"]):
    try:
        E_A = ellipse_area(major_axis, minor_axis)
        print(ellipse_area_message.format(Ellipse_major_axis=major_axis, Ellipse_minor_axis=minor_axis, area=E_A))
    except (TypeError, ValueError) as e:
        print(f"Error for ellipse with major axis {major_axis}, minor axis {minor_axis}: {e}")
# ---------------------------


#----------------------------
# Shape 4: Rhombus

rhombus_diagonals = {
    "Rhombus_diagonal1" : [2, 3, "test", -1, 4.5, 1000000],
    "Rhombus_diagonal2" : [2, 3, "test", -1, 4.5, 1000000]
}
def rhombus_area(Rhombus_diagonal1, Rhombus_diagonal2):
    if not isinstance(Rhombus_diagonal1, (int, float)):
        raise TypeError("Diagonal 1 must be a number")
    if Rhombus_diagonal1 < 0:
        raise ValueError("Diagonal 1 must be a positive number")
    if not isinstance(Rhombus_diagonal2, (int, float)):
        raise TypeError("Diagonal 2 must be a number")
    if Rhombus_diagonal2 < 0:
        raise ValueError("Diagonal 2 must be a positive number")
    return (Rhombus_diagonal1 * Rhombus_diagonal2) / 2

rhombus_area_message = "Area of rhombus with diagonal1 = {Rhombus_diagonal1:.2f}, diagonal2 = {Rhombus_diagonal2:.2f} is {area:.2f}"

for diagonal1, diagonal2 in zip(rhombus_diagonals["Rhombus_diagonal1"], rhombus_diagonals["Rhombus_diagonal2"]):
    try:
        R_A = rhombus_area(diagonal1, diagonal2)
        print(rhombus_area_message.format(Rhombus_diagonal1=diagonal1, Rhombus_diagonal2=diagonal2, area=R_A))
    except (TypeError, ValueError) as e:
        print(f"Error for rhombus with diagonal1 {diagonal1}, diagonal2 {diagonal2}: {e}")
#----------------------------