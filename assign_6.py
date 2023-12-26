#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/25/2023
# This program will get user input for a list of integers,
# and display the integers in the list at the odd index.
# Additionally my program will get another input of an integer
# and will display the digits of the integers separated by commas.


# Creating a function that will display the elements at odd positions
# in a list.
def elements_at_odd_positions(list_of_elements):
    # Declaring an empty list for odd elements.
    odd_element_list = []

    # Using a For each loop to get the odd elements from the list.
    for index, element in enumerate(list_of_elements):
        # Checking if the element's index is odd.
        if (index % 2 == 1):
            # Appending the odd element to the list.
            odd_element_list.append(element)

    # Returning the odd element in the list to the function.
    return odd_element_list

# Creating a function that will display the individual digits inside
# a number using lists.
def list_of_numbers(whole_number):
    # Declaring a list to hold the individual elements.
    list_of_digits = []
    # Converting the number inputted by the user into a string
    # to iterate through its characters.
    whole_number_str = str(whole_number)

    # Using a For Each loop to get the individual elements.
    for digit in whole_number_str:
        # Appending the individual digits to the list.
        # Also converting it into an integer.
        list_of_digits.append(int(digit))

    # Returning the list to the function.
    return list_of_digits

# Main function that will allow for user input/output and also error check.
def main():
    # Getting user inputs.
    list_as_string = input("Please enter a string of integers separated by spaces: ")
    whole_number_as_string = input("Please enter a positive whole number: ")

    # Using a try catch to catch any errors.
    try:
        # Converting the user input as a string into a list of integers.
        list_as_integer = [int(element) for element in list_as_string.split()]
        # Converting the user input from a string to an integer.
        whole_number_as_integer = int(whole_number_as_string)

        # Checking if they entered a negative number and verifying numbers in list are positive.
        if whole_number_as_integer < 0 or any(num < 0 for num in list_as_integer):
            print("Please enter a positive number.")
        # Else they're positive, so call functions.
        else:
            odd_elements = elements_at_odd_positions(list_as_integer)
            separated_digits = list_of_numbers(whole_number_as_integer)

            # Displaying the digits of the user's number and the
            # elements at odd positions from their list.
            print("The elements in your list at odd positions are: {}.".format(odd_elements))
            print("The digits of your numbers are: {}.".format(separated_digits))

    # Catching any errors.
    except:
        print("Invalid input. Please try again")

if __name__ == "__main__":
    main()
