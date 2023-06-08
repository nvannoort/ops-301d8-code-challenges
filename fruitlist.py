#!/usr/bin/env python3

# Script Name:                  fruitlist
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      06/07/2023
# Purpose:                      learn how to use lists
# Assign to a variable a list of ten string elements
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'icecream', 'jackfruit']

# Print the fourth element of the list
print(my_list[3])  # Indexing in Python starts from 0, so the fourth element is at index 3

# Print the sixth through tenth element of the list
print(my_list[5:])  # The slicing syntax in Python is [start:stop), where start is inclusive and stop is exclusive

# Change the value of the seventh element to “onion”
my_list[6] = 'onion'  # Indexing in Python starts from 0, so the seventh element is at index 6
print(my_list)
