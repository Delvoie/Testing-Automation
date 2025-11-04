"""
Name: Lucas Delvoie 
Date: October 4, 2025
Type: Python Program - ICE 2: Fundamentals of Testing
Description: This program finds the minimum value from a list of integers.
"""

# finds the minimum value in a list of only numbers retunrs the minimum value and error messages for invalid inputs
def find_minimum(integer_list):

    # first Check if list is empty
    if len(integer_list) == 0:
        raise ValueError("List is empty")
    
    # Check if all values are integers
    # Inspired by https://stackoverflow.com/questions/13252333/check-if-all-elements-of-a-list-are-of-the-same-type
    for integers in integer_list:
        if not isinstance(integers, int):
            raise ValueError(f"Error in list must contain only integers.")

    # Find and return the minimum value
    # initialize list with first value
    minimum = integer_list[0]
    # for loop to check each value in the list
    for num in integer_list:
        #compare each value to the minimum value
        if num < minimum:
            minimum = num
    # return the minimum value
    return minimum


def main():
    
    # Test cases as defined in the assignment
    # Used ai to populate test cases from assignment
    test_cases = [
        # Test Case 1: Basic functionality
        ([90], "1A"),
        ([12, 10], "1B"),
        ([10, 12], "1C"),
        ([12, 14, 36], "1D"),
        ([36, 14, 12], "1E"),
        ([14, 12, 36], "1F"),
        
        # list is empty (not passed)
        ([], "2A"),
        
        # alot of numbers
        ([10, 23, 34, 81, 97], "3A"),
        ([97, 81, 34, 23, 10], "3B"),
        
        # positive and negative integers
        ([10, -2, 5, 23], "4A"),
        ([10, -2, -24, 4], "4B"),
        
        # All negative
        ([-23, -31, -45, -56], "5A"),
        ([-6, -203, -2, -78], "5B"),
        
        # test for float (not passed)
        ([23, 34.56, 67, 33], "6A"),
        
        # test for string (not passed)
        ([23, "hi", 32, 1], "7A"),
        ([12, "&", "*", "34m", "!"], "7B"),
        
        # replicate numbers
        ([3, 4, 6, 9, 6], "8A"),
        ([13, 6, 6, 9, 15], "8B"),
        
        # large numbers
        ([530, 4294967297, 97, 23, 46], "9A"),
    ]
    
    print("-------------------------------------")
    
    # Run each test case
    for test_input, test_id in test_cases:
        print(f"Test Id: {test_id}:")
        print(f"Input: {test_input}")
        
        try:
            result = find_minimum(test_input)
            print(f"Output: {result}")
        except ValueError as error:
            print(f"Output: {error}")
        # Failed
        except Exception as unexpected_error:
            print(f"Output failed unexpectedly: {unexpected_error}")

if __name__ == "__main__":
    main()
