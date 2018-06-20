# -*- coding: utf-8 -*-
"""
Task 3

Assumption: Each ‘Enter’ indicates a sequence, characters between two ‘*’ means subsequence.
Extending from task 2, Task3.py displays an error message indicating which subsequence is invalid and decodes the valid subsequences into the corresponding characters. 
Especially, if the input contains chain of ‘*’, the subsequence between two ‘*’ is nothing thus there will be no error message printed.

@author: KEWEN DENG
"""

# Step 1.1 : Build Characters to be values in Dictionary
dict_cha = []
for cha in range(65,91):
    dict_cha.append(chr(cha))
for cha in range(0,10):
    dict_cha.append(str(cha))

# Step 1.2 : Build Morse Code to be keys in Dictionary
dict_mc = [ '01', '1000',  '1010',   '100',     '0',  '0010',   '110',  '0000',    '00',  '0111',   '101',  '0100',
            '11',   '10',   '111',  '0110',  '1101',   '010',   '000',     '1',   '001',  '0001',   '011',  '1001',
          '1011', '1100', '11111', '01111', '00111', '00011', '00001', '00000', '10000', '11000', '11100', '11110']

# Step 1.3 : Zip Morse Code(keys) and Character(values) to Dictionary
dictionary = dict(list(zip(dict_mc, dict_cha)))

# Step 2.1 : Read first input as an initialization
user_input = input("Please enter a sentence comprised of the 26 letters and/or 9 digits. Press Enter to quit.")

# Step 2.2 : Loop for Read and Print untill user would like to terminate
while user_input != '':
    print("Oringinal message : ", user_input) # Read input and print the original message
    
    # Step 3.1 : Initializion for decode
    output = '' # output is the answer to print
    morse = '' # morse is the subsequence to decode
    user_input = user_input + '*' # put an * to indicate the end of a sequence
    
    # Step 3.2 : Loop for cut down long subsequence to single word
    for letter in user_input: # letter is every single character in input
        if letter != '*': # extract subsequence from a whole sequence
            morse = morse + letter
        elif morse != '' : # judge the subsequence is valid or not
            if morse in dictionary.keys() : # if the subsequence is valid, add it to output
                output = output + dictionary[morse]
            else: # if the subsequence is invalid, send an error message
                print(morse, " is invalid!")
            morse = '' # clear morse for next subsequence 
    
    # Step 3.3 : Print output only if the output exist
    if output != '' :
        print("Translated message : ", output, sep = '')
    
    user_input = input("Please enter a sentence comprised of the 26 letters and/or 9 digits. Press Enter to quit.")

    
    
