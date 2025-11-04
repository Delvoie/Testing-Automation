# Date: Oct 29, 2025
# Name: test_Minimum.py - ICE3 Test
# Programmer:  Lucas
# Description: Unit tests for find_minimum() function with subcases (A, B, C, etc.)
#              

import unittest
from ..app.minimum import find_minimum

class TestMinimum(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        print("setUp")

    def tearDown(self):
        """Clean up after each test method."""
        print("tearDown\n")


    # Test Case 1: Very short list (size 1, 2, or 3)
    def test_case_1A(self):
        print("Running Test Case 1A: Size 1")
        self.assertEqual(find_minimum([90]), 90)

    def test_case_1B(self):
        print("Running Test Case 1B: Size 2, min at index 1")
        self.assertEqual(find_minimum([12, 10]), 10)

    def test_case_1C(self):
        print("Running Test Case 1C: Size 2, min at index 0")
        self.assertEqual(find_minimum([10, 12]), 10)

    def test_case_1D(self):
        print("Running Test Case 1D: Size 3, min at index 0")
        self.assertEqual(find_minimum([12, 14, 36]), 12)

    def test_case_1E(self):
        print("Running Test Case 1E: Size 3, min at index 2")
        self.assertEqual(find_minimum([36, 14, 12]), 12)

    def test_case_1F(self):
        print("Running Test Case 1F: Size 3, min at index 1")
        self.assertEqual(find_minimum([14, 12, 36]), 12)


    # Test Case 2: Empty list
    def test_case_2A(self):
        print("Running Test Case 2A: Empty list")
        with self.assertRaises(ValueError):
            find_minimum([])

    # Test Case 3: Minimum at first or last position
    def test_case_3A(self):
        print("Running Test Case 3A: Min at first position")
        self.assertEqual(find_minimum([10, 23, 34, 81, 97]), 10)

    def test_case_3B(self):
        print("Running Test Case 3B: Min at last position")
        self.assertEqual(find_minimum([97, 81, 34, 23, 10]), 10)


    # Test Case 4: Minimum is negative
    def test_case_4A(self):
        print("Running Test Case 4A: One negative (min)")
        self.assertEqual(find_minimum([10, -2, 5, 23]), -2)

    def test_case_4B(self):
        print("Running Test Case 4B: Multiple negatives, min is most negative")
        self.assertEqual(find_minimum([10, -2, -24, 4]), -24)


    # Test Case 5: All elements are negative
    def test_case_5A(self):
        print("Running Test Case 5A: All negative, min is last")
        self.assertEqual(find_minimum([-23, -31, -45, -56]), -56)

    def test_case_5B(self):
        print("Running Test Case 5B: All negative, min is middle")
        self.assertEqual(find_minimum([-6, -203, -2, -78]), -203)


    # Test Case 6: List with real numbers (floats)
    def test_case_6A(self):
        print("Running Test Case 6A: Float values (invalid)")
        with self.assertRaises(ValueError):
            find_minimum([23, 34.56, 67, 33])


    # Test Case 7: Alphabetic and special characters
    def test_case_7A(self):
        print("Running Test Case 7A: Mixed alphanumeric and special chars")
        with self.assertRaises(ValueError):
            find_minimum([23, "hi", 32, 1])

    def test_case_7B(self):
        print("Running Test Case 7B: All special characters")
        with self.assertRaises(ValueError):
            find_minimum(["12", "&", "*", "34m", "!"])

    # Additional: Test Case 7C - Boolean values (should fail)
    def test_case_7C(self):
        print("Running Test Case 7C: Boolean values (invalid)")
        with self.assertRaises(ValueError):
            find_minimum([True, False, 10, 5])


    # Test Case 8: Duplicate elements
    def test_case_8A(self):
        print("Running Test Case 8A: Duplicates, min is first unique")
        self.assertEqual(find_minimum([3, 4, 6, 9, 6]), 3)

    def test_case_8B(self):
        print("Running Test Case 8B: Duplicates, min is repeated")
        self.assertEqual(find_minimum([13, 6, 6, 9, 15]), 6)


    # Test Case 9: Very large integers (Python handles big ints)
    def test_case_9A(self):
        print("Running Test Case 9A: Large integers (within int limits)")
        self.assertEqual(find_minimum([530, 429449672, 97, 23, 46, 59]), 23)

    # Additional: Test Case 9B - Extremely large integers (Python3 supports arbitrary precision)
    def test_case_9B(self):
        print("Running Test Case 9B: Extremely large integers (Python handles them)")
        huge_num = 10**100
        self.assertEqual(find_minimum([huge_num, huge_num - 1, 0]), 0)


if __name__ == '__main__':
    unittest.main()