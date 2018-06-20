# -*- coding: utf-8 -*-
"""
Task 2

Assumption: If the user would like to terminate, type nothing and press ‘Enter’.

In this task, I designed a WHILE loop for user to input multiple Morse Code sequences. 
If the user wish to terminate, press ‘Enter’ then the program will stop automatically. 
According to the assignment requirements, the program prints every input originally.

@author: KEWEN DENG
"""

# Step 2.1 : Read first input as an initialization
user_input = input("Please enter a sentence comprised of the 26 letters and/or 9 digits. Press Enter to quit.")

# Step 2.2 : Loop for Read and Print untill user would like to terminate 
while user_input != '':
    print("Oringinal message : ", user_input) # Read input and print the original message
    user_input = input("Please enter a sentence comprised of the 26 letters and/or 9 digits. Press Enter to quit.")
