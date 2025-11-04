# Date: Sept 24, 2025
# Name: "Password Generator"
# Programmer: Lucas & Alyssa
# Description: Generates a password with certain parameters

# Imports
import random
from string import ascii_letters, digits, punctuation

# Min and Max variables
MIN_LENGTH = 8
MAX_LENGTH = 100

# Function to validate user input
def valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f'Please enter a value between {min_value} and {max_value}')
                return valid_input(prompt, min_value, max_value)
        except ValueError:
            print("Please enter a numeric value.")
            return valid_input(prompt, min_value, max_value)


# Copilot autocomplete recommendation: Generates a password assigning each character type a random probability.
# Uses ascii_letters, digits, and punctuation from the string module for character selection.
def generate_password(length, letters, num_digits, special):
    password_chars = (
            random.choices(ascii_letters, k=letters) +
            random.choices(digits, k=num_digits) +
            random.choices(punctuation, k=special) +
            random.choices(ascii_letters + digits + punctuation, k=length - (letters + num_digits + special))
    )

    # Shuffles password for better security
    random.shuffle(password_chars)
    # Joins letters, digits, and special characters
    return ''.join(password_chars)

# Main function
def main_function():
    print("Random Password Generator\n")
    # Prompt user and use min and max length parameters
    length = valid_input(f'Enter the length of the password between {MIN_LENGTH}, {MAX_LENGTH}: ', MIN_LENGTH, MAX_LENGTH)
    # Makes sure that the sum of letters, digits, and special characters fit in parameters
    letters = valid_input(f'Enter the number of letters (0-{length}): ', 0, length)
    num_digits = valid_input(f'Enter the number of digits (0-{length - letters}): ', 0, length - letters)
    special = valid_input(f'Enter the number of special characters (0-{length - letters - num_digits}): ', 0, length - letters - num_digits)

    # Check if the sum of letters, digits, and special characters can fit within the length
    if length >= letters + num_digits + special:
        password = generate_password(length, letters, num_digits, special)
        print(f'Your generated password is: \n{password}')
    else:
        print("Error: The sum of letters, digits, and special characters exceeds the total length.")


if __name__ == "__main__":
    main_function()