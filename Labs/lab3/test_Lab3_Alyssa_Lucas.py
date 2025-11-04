# Date: Oct 27, 2025
# Name: "test_Lab3_Alyssa_Lucas.py - Area Calculation Tester"
# Programmer: Alyssa and Lucas
# Description: unit tests for Shape Area Calculator (Lab3).

# imports
import unittest
from math import pi
import sys
from pathlib import Path

# Ensure the current directory is in the Python path
current_dir = Path(__file__).parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))


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
        cls.int_value = 2
        cls.float_value = 2.5
        cls.negative_value = -3
        cls.large_value = 99999.0
        cls.complex_value = 2 + 5j
        cls.expression_result = 1.5 + 1.5
        cls.zero_value = 0
        cls.list_value = [5]
        cls.tuple_value = (3,)
        cls.dict_value = {4: "radius"}
        cls.none_value = None
        cls.bool_true = True
        cls.bool_false = False
        cls.string_value = "radius"
        cls.invalid_operation = lambda: 1 + "radius"
        print("SetupClass Circle ")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Circle ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_int_value(self):
        result = calculate_circle_area(self.int_value)
        expected = pi * self.int_value ** 2
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when radius of circle is int")

    def test_float_value(self):
        result = calculate_circle_area(self.float_value)
        expected = pi * self.float_value ** 2
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when radius of circle is float")

    def test_negative_value(self):
        self.assertRaises(ValueError, calculate_circle_area, self.negative_value)
        print(f"End of Test: Exception raised when radius of circle is negative")

    def test_large_value(self):
        result = calculate_circle_area(self.large_value)
        expected = pi * self.large_value ** 2
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when radius of circle is large value")

    def test_complex_value(self):
        self.assertRaises(TypeError, calculate_circle_area, self.complex_value)
        print(f"End of Test: Exception raised when radius of circle is complex number")

    def test_expression_result(self):
        result = calculate_circle_area(self.expression_result)
        expected = pi * self.expression_result ** 2
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when radius of circle is expression result")

    def test_zero_value(self):
        result = calculate_circle_area(self.zero_value)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when radius of circle is zero")

    def test_list_value(self):
        self.assertRaises(TypeError, calculate_circle_area, self.list_value)
        print(f"End of Test: Exception raised when radius of circle is list")

    def test_tuple_value(self):
        self.assertRaises(TypeError, calculate_circle_area, self.tuple_value)
        print(f"End of Test: Exception raised when radius of circle is tuple")

    def test_dict_value(self):
        self.assertRaises(TypeError, calculate_circle_area, self.dict_value)
        print(f"End of Test: Exception raised when radius of circle is dict")

    def test_none_value(self):
        self.assertRaises(TypeError, calculate_circle_area, self.none_value)
        print(f"End of Test: Exception raised when radius of circle is None")

    def test_bool_true(self):
        self.assertRaises(TypeError, calculate_circle_area, self.bool_true)
        print(f"End of Test: Exception raised when radius of circle is True")

    def test_bool_false(self):
        self.assertRaises(TypeError, calculate_circle_area, self.bool_false)
        print(f"End of Test: Exception raised when radius of circle is False")

    def test_string_value(self):
        self.assertRaises(TypeError, calculate_circle_area, self.string_value)
        print(f"End of Test: Exception raised when radius of circle is string")

    def test_invalid_operation(self):
        self.assertRaises(TypeError, self.invalid_operation)
        print(f"End of Test: Exception raised when radius involves invalid operation (1 + string)")


# Trapezium tests
class TestTrapezium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.int_value = 2
        cls.float_value = 2.5
        cls.negative_value = -3
        cls.large_value = 99999.0
        cls.complex_value = 2 + 5j
        cls.expression_result = 1.5 + 1.5
        cls.zero_value = 0
        cls.list_value = [5]
        cls.tuple_value = (3,)
        cls.dict_value = {4: "base"}
        cls.none_value = None
        cls.bool_true = True
        cls.bool_false = False
        cls.string_value = "base"
        cls.invalid_operation = lambda: 1 + "base"
        cls.valid_base = 10
        cls.valid_top = 20
        cls.valid_height = 5
        print("SetupClass Trapezium ")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Trapezium ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_int_values(self):
        result = calculate_trapezium_area(self.int_value, self.int_value, self.int_value)
        expected = 0.5 * (self.int_value + self.int_value) * self.int_value
        self.assertEqual(result, expected)
        print(f"End of Test: Test area when trapezium dimensions are int")

    def test_float_values(self):
        result = calculate_trapezium_area(self.float_value, self.float_value, self.float_value)
        expected = 0.5 * (self.float_value + self.float_value) * self.float_value
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when trapezium dimensions are float")

    def test_negative_base(self):
        self.assertRaises(ValueError, calculate_trapezium_area, self.negative_value, self.valid_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium base is negative")

    def test_negative_top(self):
        self.assertRaises(ValueError, calculate_trapezium_area, self.valid_base, self.negative_value, self.valid_height)
        print(f"End of Test: Exception raised when trapezium top is negative")

    def test_negative_height(self):
        self.assertRaises(ValueError, calculate_trapezium_area, self.valid_base, self.valid_top, self.negative_value)
        print(f"End of Test: Exception raised when trapezium height is negative")

    def test_large_values(self):
        result = calculate_trapezium_area(self.large_value, self.large_value, self.large_value)
        expected = 0.5 * (self.large_value + self.large_value) * self.large_value
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when trapezium dimensions are large values")

    def test_complex_base(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.complex_value, self.valid_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium base is complex number")

    def test_expression_result(self):
        result = calculate_trapezium_area(self.expression_result, self.expression_result, self.expression_result)
        expected = 0.5 * (self.expression_result + self.expression_result) * self.expression_result
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when trapezium dimensions are expression results")

    def test_zero_height(self):
        result = calculate_trapezium_area(self.valid_base, self.valid_top, self.zero_value)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when trapezium height is zero")

    def test_list_base(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.list_value, self.valid_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium base is list")

    def test_tuple_top(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.valid_base, self.tuple_value, self.valid_height)
        print(f"End of Test: Exception raised when trapezium top is tuple")

    def test_dict_height(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.valid_base, self.valid_top, self.dict_value)
        print(f"End of Test: Exception raised when trapezium height is dict")

    def test_none_base(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.none_value, self.valid_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium base is None")

    def test_bool_values(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.bool_true, self.bool_true, self.bool_true)
        print(f"End of Test: Exception raised when trapezium dimensions are boolean")

    def test_string_base(self):
        self.assertRaises(TypeError, calculate_trapezium_area, self.string_value, self.valid_top, self.valid_height)
        print(f"End of Test: Exception raised when trapezium base is string")

    def test_invalid_operation(self):
        self.assertRaises(TypeError, self.invalid_operation)
        print(f"End of Test: Exception raised when trapezium involves invalid operation (1 + string)")


# Ellipse tests
class TestEllipse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.int_value = 2
        cls.float_value = 2.5
        cls.negative_value = -3
        cls.large_value = 99999.0
        cls.complex_value = 2 + 5j
        cls.expression_result = 1.5 + 1.5
        cls.zero_value = 0
        cls.list_value = [5]
        cls.tuple_value = (3,)
        cls.dict_value = {4: "axis"}
        cls.none_value = None
        cls.bool_true = True
        cls.bool_false = False
        cls.string_value = "axis"
        cls.invalid_operation = lambda: 1 + "axis"
        cls.valid_major = 10
        cls.valid_minor = 5
        print("SetupClass Ellipse ")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Ellipse ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_int_values(self):
        result = calculate_ellipse_area(self.int_value, self.int_value)
        expected = pi * self.int_value * self.int_value
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when ellipse axes are int")

    def test_float_values(self):
        result = calculate_ellipse_area(self.float_value, self.float_value)
        expected = pi * self.float_value * self.float_value
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when ellipse axes are float")

    def test_negative_major(self):
        self.assertRaises(ValueError, calculate_ellipse_area, self.negative_value, self.valid_minor)
        print(f"End of Test: Exception raised when ellipse major axis is negative")

    def test_negative_minor(self):
        self.assertRaises(ValueError, calculate_ellipse_area, self.valid_major, self.negative_value)
        print(f"End of Test: Exception raised when ellipse minor axis is negative")

    def test_large_values(self):
        result = calculate_ellipse_area(self.large_value, self.large_value)
        expected = pi * self.large_value * self.large_value
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when ellipse axes are large values")

    def test_complex_major(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.complex_value, self.valid_minor)
        print(f"End of Test: Exception raised when ellipse major axis is complex number")

    def test_expression_result(self):
        result = calculate_ellipse_area(self.expression_result, self.expression_result)
        expected = pi * self.expression_result * self.expression_result
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when ellipse axes are expression results")

    def test_zero_minor(self):
        result = calculate_ellipse_area(self.valid_major, self.zero_value)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when ellipse minor axis is zero")

    def test_list_major(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.list_value, self.valid_minor)
        print(f"End of Test: Exception raised when ellipse major axis is list")

    def test_tuple_minor(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.valid_major, self.tuple_value)
        print(f"End of Test: Exception raised when ellipse minor axis is tuple")

    def test_dict_major(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.dict_value, self.valid_minor)
        print(f"End of Test: Exception raised when ellipse major axis is dict")

    def test_none_minor(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.valid_major, self.none_value)
        print(f"End of Test: Exception raised when ellipse minor axis is None")

    def test_bool_values(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.bool_true, self.bool_true)
        print(f"End of Test: Exception raised when ellipse axes are boolean")

    def test_string_major(self):
        self.assertRaises(TypeError, calculate_ellipse_area, self.string_value, self.valid_minor)
        print(f"End of Test: Exception raised when ellipse major axis is string")

    def test_invalid_operation(self):
        self.assertRaises(TypeError, self.invalid_operation)
        print(f"End of Test: Exception raised when ellipse involves invalid operation (1 + string)")


# Rhombus tests
class TestRhombus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.int_value = 2
        cls.float_value = 2.5
        cls.negative_value = -3
        cls.large_value = 99999.0
        cls.complex_value = 2 + 5j
        cls.expression_result = 1.5 + 1.5
        cls.zero_value = 0
        cls.list_value = [5]
        cls.tuple_value = (3,)
        cls.dict_value = {4: "diagonal"}
        cls.none_value = None
        cls.bool_true = True
        cls.bool_false = False
        cls.string_value = "diagonal"
        cls.invalid_operation = lambda: 1 + "diagonal"
        cls.valid_diagonal1 = 10
        cls.valid_diagonal2 = 20
        print("SetupClass Rhombus ")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Rhombus ")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_int_values(self):
        result = calculate_rhombus_area(self.int_value, self.int_value)
        expected = 0.5 * self.int_value * self.int_value
        self.assertEqual(result, expected)
        print(f"End of Test: Test area when rhombus diagonals are int")

    def test_float_values(self):
        result = calculate_rhombus_area(self.float_value, self.float_value)
        expected = 0.5 * self.float_value * self.float_value
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when rhombus diagonals are float")

    def test_negative_diagonal1(self):
        self.assertRaises(ValueError, calculate_rhombus_area, self.negative_value, self.valid_diagonal2)
        print(f"End of Test: Exception raised when rhombus diagonal1 is negative")

    def test_negative_diagonal2(self):
        self.assertRaises(ValueError, calculate_rhombus_area, self.valid_diagonal1, self.negative_value)
        print(f"End of Test: Exception raised when rhombus diagonal2 is negative")

    def test_large_values(self):
        result = calculate_rhombus_area(self.large_value, self.large_value)
        expected = 0.5 * self.large_value * self.large_value
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when rhombus diagonals are large values")

    def test_complex_diagonal1(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.complex_value, self.valid_diagonal2)
        print(f"End of Test: Exception raised when rhombus diagonal1 is complex number")

    def test_expression_result(self):
        result = calculate_rhombus_area(self.expression_result, self.expression_result)
        expected = 0.5 * self.expression_result * self.expression_result
        self.assertAlmostEqual(result, expected, places=12)
        print(f"End of Test: Test area when rhombus diagonals are expression results")

    def test_zero_diagonal1(self):
        result = calculate_rhombus_area(self.zero_value, self.valid_diagonal2)
        self.assertEqual(result, 0.0)
        print(f"End of Test: Test area when rhombus diagonal1 is zero")

    def test_list_diagonal1(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.list_value, self.valid_diagonal2)
        print(f"End of Test: Exception raised when rhombus diagonal1 is list")

    def test_tuple_diagonal2(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.valid_diagonal1, self.tuple_value)
        print(f"End of Test: Exception raised when rhombus diagonal2 is tuple")

    def test_dict_diagonal1(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.dict_value, self.valid_diagonal2)
        print(f"End of Test: Exception raised when rhombus diagonal1 is dict")

    def test_none_diagonal2(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.valid_diagonal1, self.none_value)
        print(f"End of Test: Exception raised when rhombus diagonal2 is None")

    def test_bool_values(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.bool_true, self.bool_true)
        print(f"End of Test: Exception raised when rhombus diagonals are boolean")

    def test_string_diagonal1(self):
        self.assertRaises(TypeError, calculate_rhombus_area, self.string_value, self.valid_diagonal2)
        print(f"End of Test: Exception raised when rhombus diagonal1 is string")

    def test_invalid_operation(self):
        self.assertRaises(TypeError, self.invalid_operation)
        print(f"End of Test: Exception raised when rhombus involves invalid operation (1 + string)")


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
    choice = ""

    while choice != "q":
        print("\nPlease enter one of the following options:")
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