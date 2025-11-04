# Date: Oct 29, 2025
# Name: "test_Minimum.py - ICE3 Test"
# Programmer: Lucas
# Description: Unit test to find the minimum value in a list of integers

import unittest
from ..app.minimum import find_minimum


class TestMinimum(unittest.TestCase):
    # Test Case 1: A very short list (of inputs) with the size of 1, 2, or 3 elements.
    def test_case_1(self):
        self.assertEqual(find_minimum([90, 91]), 90, "Should be 90")

    #Test Case 2: An empty list i.e., of size 0.
    def test_case_2(self):
        self.assertRaises(ValueError, find_minimum, [])

    # Test Case 3: A list where the minimum element is the first or last element.
    def test_case_3(self):
        self.assertEqual(find_minimum([180, 200, 90, 90]), 90, "Should be 90")

    # Test Case 4: A list where the minimum element is negative.
    def test_case_4(self):
        self.assertEqual(find_minimum([-21, -10, 1]), -21, "Should be -21")

    # Test Case 5: A list where all elements are negative.
    def test_case_5(self):
        self.assertEqual(find_minimum([-3, -2, -1, 0]), -3, "Should be -3")

    # Test Case 6: A list where some elements are real numbers.
    def test_case_6(self):
        with self.assertRaises(ValueError):
            self.assertFalse(find_minimum(["a", "!", "h", ")"]))

    # Test Case 7: A list where some elements are alphabetic characters and special characters.
    def test_case_7(self):
        with self.assertRaises(ValueError):
            self.assertFalse(find_minimum(["a", "!", "h", ")"]))

    # Test Case 8: A list with duplicate elements.
    def test_case_8(self):
        self.assertEqual(find_minimum([90, 91, 90, 180]), 90, "should be 90")

    # Test Case 9: A list where one element has a value greater than the maximum permissible
    # limit of an integer.
    def test_case_9(self):
        print("Running Test Case 9B: Extremely large integers (Python handles them)")
        huge_num = 10**100
        self.assertEqual(find_minimum([huge_num, huge_num - 1, 0]), 0)

#-----------------------------------
# Additional Test Cases

    # Test Case 10: A list with only one element.
    def test_case_10(self):
        self.assertEqual(find_minimum([42]), 42, "Should be 42")

    # Test Case 13: A list where all elements are the same.
    def test_case_13(self):
        self.assertEqual(find_minimum([5, 5, 5, 5]), 5, "Should be 5")

    # Test Case 15: A list with floating-point numbers.
    def test_case_15(self):
        with self.assertRaises(ValueError):
            find_minimum([1.5, 2.5, 3.5])

    # Test Case 16: A list with zero as the minimum value.
    def test_case_16(self):
        self.assertEqual(find_minimum([0, 5, 10, 15]), 0, "Should be 0")

    # Test Case 17: A list with boolean values.
    def test_case_17(self):
        with self.assertRaises(ValueError):
            find_minimum([True, False, 1, 0])



if __name__ == '__main__':
    unittest.main()
