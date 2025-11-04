# Date: Oct 27, 2025
# Name: "test_Lab3_Alyssa_Lucas.py - Area Calculation Tester"
# Programmer: Alyssa and Lucas
# Description: unit tests for Shape Area Calculator (Lab3).

# imports
import unittest
from math import pi
# import shape area functions
from Lab3_Alyssa_Lucas_app import (
    calculate_circle_area,
    calculate_trapezium_area,
    calculate_ellipse_area,
    calculate_rhombus_area
)

# Circle tests
class TestCircle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures before any test methods."""
        cls.valid_radius = 5
        cls.zero_radius = 0
        cls.float_radius = 3.14
        cls.negative_radius = -1
        cls.invalid_type = "invalid"
        cls.large_radius = 10000.0
        print("SetupClass Circle ")


    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Circle ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_valid_positive(self):
        result = calculate_circle_area(self.valid_radius)
        expected = pi * self.valid_radius ** 2
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when radius of circle is >= 0")

    def test_zero_radius(self):
        result = calculate_circle_area(self.zero_radius)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when radius of circle is 0")

    def test_float_radius(self):
        result = calculate_circle_area(self.float_radius)
        expected = pi * (self.float_radius ** 2)
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when radius of circle is float")

    def test_negative_radius(self):
        self.assertRaises(ValueError, calculate_circle_area, self.negative_radius)
        print(f"End of Test: Exception raised when radius of circle < 0")

    def test_invalid_type(self):
        self.assertRaises(TypeError, calculate_circle_area, self.invalid_type)
        print(f"End of Test: Exception raised when radius of circle is invalid type")

    def test_large_radius(self):
        result = calculate_circle_area(self.large_radius)
        expected = pi * (self.large_radius ** 2)
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when radius of circle is large value")

# Trapezium tests
class TestTrapezium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_base = 10
        cls.valid_top = 20
        cls.valid_height = 5
        cls.zero_height = 0
        cls.float_base = 10.5
        cls.float_top = 20.3
        cls.float_height = 5.1
        cls.negative_base = -10
        cls.negative_top = -20
        cls.negative_height = -5
        cls.invalid_type = "10"
        cls.large_base = 10000
        cls.large_top = 20000
        cls.large_height = 5000
        print("SetupClass Trapezium ")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Trapezium ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_valid_trapezium(self):
        result = calculate_trapezium_area(self.valid_base, self.valid_top, self.valid_height)
        self.assertEqual(result, 75.0)
        print(f"End of Test: Test area when trapezium dimensions are valid")

    def test_zero_height(self):
        result = calculate_trapezium_area(self.valid_base, self.valid_top, self.zero_height)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when trapezium height is 0")

    def test_float_dimensions(self):
        result = calculate_trapezium_area(self.float_base, self.float_top, self.float_height)
        self.assertAlmostEqual(result, 0.5 * (self.float_base + self.float_top) * self.float_height, places=12)
        print(f"End of Test: Test area when trapezium dimensions are float")

    def test_negative_base(self):
        self.assertRaises(ValueError, calculate_trapezium_area, self.negative_base, self.valid_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium base < 0")

    def test_negative_top(self):
        self.assertRaises(ValueError, calculate_trapezium_area, self.valid_base, self.negative_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium top < 0")

    def test_negative_height(self):
        self.assertRaises(ValueError, calculate_trapezium_area, self.valid_base, self.valid_top, self.negative_height)
        print(f"End of Test: Exception raised when trapezium height < 0")

    def test_invalid_type_base(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.invalid_type, self.valid_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium dimension is invalid type")

    def test_large_values(self):
        result = calculate_trapezium_area(self.large_base, self.large_top, self.large_height)
        self.assertEqual(result, 75000000.0)
        print(f"End of Test: Test area when trapezium dimensions are large values")

# Ellipse tests
class TestEllipse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_major = 10
        cls.valid_minor = 5
        cls.zero_minor = 0
        cls.float_major = 9.2
        cls.float_minor = 4.7
        cls.negative_major = -10
        cls.negative_minor = -5
        cls.invalid_type = "5"
        cls.large_major = 10000.0
        cls.large_minor = 5000.0
        print("SetupClass Trapezium ")


    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Trapezium ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_valid_ellipse(self):
        result = calculate_ellipse_area(self.valid_major, self.valid_minor)
        expected = pi * self.valid_major * self.valid_minor
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when ellipse axes are valid")

    def test_zero_minor(self):
        result = calculate_ellipse_area(self.valid_major, self.zero_minor)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when ellipse minor axis is 0")

    def test_float_axes(self):
        result = calculate_ellipse_area(self.float_major, self.float_minor)
        expected = pi * self.float_major * self.float_minor
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when ellipse axes are float")

    def test_negative_major(self):
        self.assertRaises(ValueError, calculate_ellipse_area, self.negative_major, self.valid_minor)
        print(f"End of Test: Exception raised when ellipse major axis < 0")

    def test_negative_minor(self):
        self.assertRaises(ValueError, calculate_ellipse_area, self.valid_major, self.negative_minor)
        print(f"End of Test: Exception raised when ellipse minor axis < 0")

    def test_invalid_type(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.valid_major, self.invalid_type)
        print(f"End of Test: Exception raised when ellipse axis is invalid type")

    def test_large_axes(self):
        result = calculate_ellipse_area(self.large_major, self.large_minor)
        expected = pi * self.large_major * self.large_minor
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when ellipse axes are large values")

# Rhombus tests
class TestRhombus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.valid_diagonal1 = 10
        cls.valid_diagonal2 = 20
        cls.zero_diagonal = 0
        cls.float_diagonal1 = 10.5
        cls.float_diagonal2 = 20.3
        cls.negative_diagonal1 = -10
        cls.negative_diagonal2 = -20
        cls.invalid_type = "20"
        cls.large_diagonal1 = 10000
        cls.large_diagonal2 = 20000
        print("SetupClass Rhombus ")


    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Rhombus ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_valid_rhombus(self):
        result = calculate_rhombus_area(self.valid_diagonal1, self.valid_diagonal2)
        self.assertEqual(result, 100.0)
        print(f"End of Test: Test area when rhombus diagonals are valid")

    def test_zero_diagonal1(self):
        result = calculate_rhombus_area(self.zero_diagonal, self.valid_diagonal2)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when rhombus diagonal is 0")

    def test_float_diagonals(self):
        result = calculate_rhombus_area(self.float_diagonal1, self.float_diagonal2)
        self.assertAlmostEqual(result, 0.5 * self.float_diagonal1 * self.float_diagonal2, places=12)
        print(f"End of Test: Test area when rhombus diagonals are float")

    def test_negative_diagonal1(self):
        self.assertRaises(ValueError, calculate_rhombus_area, self.negative_diagonal1, self.valid_diagonal2)
        print(f"End of Test: Exception raised when rhombus diagonal1 < 0")

    def test_negative_diagonal2(self):
        self.assertRaises(ValueError, calculate_rhombus_area, self.valid_diagonal1, self.negative_diagonal2)
        print(f"End of Test: Exception raised when rhombus diagonal2 < 0")

    def test_invalid_type(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.valid_diagonal1, self.invalid_type)
        print(f"End of Test: Exception raised when rhombus diagonal is invalid type")

    def test_large_diagonals(self):
        result = calculate_rhombus_area(self.large_diagonal1, self.large_diagonal2)
        self.assertEqual(result, 100000000.0)
        print(f"End of Test: Test area when rhombus diagonals are large values")


def run_tests(shape):
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    if shape == 'c':
        suite = loader.loadTestsFromTestCase(TestCircle)
    elif shape == 't':
        suite = loader.loadTestsFromTestCase(TestTrapezium)
    elif shape == 'e':
        suite = loader.loadTestsFromTestCase(TestEllipse)
    elif shape == 'r':
        suite = loader.loadTestsFromTestCase(TestRhombus)
    else:
        return

    result = runner.run(suite)
    print(f"\nTests passed: {result.testsRun - len(result.failures) - len(result.errors)} / {result.testsRun}")


def main():
    """Main function to run menu-driven test suite."""
    print("-"*60)
    print(" "*15 + "Area of a Shape Tester")
    print("-"*60)
    choice = ""

    while choice != "q":
        print("\n📋 Select shape to test:")
        print("  'C' Circle")
        print("  'T' Trapezium")
        print("  'E' Ellipse")
        print("  'R' Rhombus")
        print("  'A' All Shapes")
        print("  'Q' Quit")
        choice = input("What would you like to do? ").lower().strip()
    
        if choice == "c":
            run_tests('c')
        elif choice == "t":
            run_tests('t')
        elif choice == "e":
            run_tests('e')
        elif choice == "r":
            run_tests('r')
        elif choice == "a":
            for shape in ['c', 't', 'e', 'r']:
                run_tests(shape)

        # Exit message
        elif choice == 'q':
            print("Exiting Shape Tester...")
        else:
            print("\nInvalid choice. Please enter a valid letter.")


if __name__ == "__main__":
    main()