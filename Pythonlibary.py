#!/usr/bin/env python3

# Script Name:                  Ops301d8 Day 12
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      06/14/2023
# Purpose:                      Start to learn Python

# import library

import requests

# Prompt the user to type a string input as the variable for your destination URL
url = input("Please enter your destination URL: ")

# Prompt the user to select a HTTP Method
print("\nPlease select a HTTP Method from the following options:")
print("GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS")
http_method = input().upper()

# Print the request
print(f"\nYou're about to send a {http_method} request to {url}. Do you want to proceed? (Y/N)")
confirm = input().upper()

if confirm == "Y":
    if http_method == 'GET':
        response = requests.get(url)
    elif http_method == 'POST':
        response = requests.post(url)
    elif http_method == 'PUT':
        response = requests.put(url)
    elif http_method == 'DELETE':
        response = requests.delete(url)
    elif http_method == 'HEAD':
        response = requests.head(url)
    elif http_method == 'PATCH':
        response = requests.patch(url)
    elif http_method == 'OPTIONS':
        response = requests.options(url)
    else:
        print("Invalid HTTP method.")
        exit()

 # Print status
    print(response.status_code)
# done