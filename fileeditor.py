#!/usr/bin/env python3

# Script Name:                  Ops301d8 Day 10
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      06/09/2023
# Purpose:                      file editor in Python

import os

# create a new file and append three lines
with open('temp.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')

# read the file and print the first line
with open('temp.txt', 'r') as file:
    lines = file.readlines()
    print(lines[0].strip())  # print first line

# delete the file
os.remove('temp.txt')
