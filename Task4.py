# -*- coding: utf-8 -*-
"""
Task 4

Extending from task 2 and task 3, Task4.py find out number of the occurrences for each of the characters,
and print them in a readable format.

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

# Step 4.1 : Initializion for count
items = list(dictionary.values()) # items is a list contains values of dictionary
count = [0] * 36 # count is the number of occurrence

# Step 2.2 : Loop for Read and Print untill user would like to terminate    
while user_input != '':
    print("Oringinal message : ", user_input)
    
    count2 = [0] * 36 # count2 is the number of occurrence of each sequence
    # Step 3.1 : Initializion for decode
    output = ''
    morse = ''
    user_input = user_input + '*'

    # Step 3.2 : Loop for cut down long subsequence to single word
    for letter in user_input:
        if letter != '*':
            morse = morse + letter
        elif morse != '' :
            if morse in dictionary.keys() :
                # Step 4.2 : Count if valid
                count[items.index(dictionary[morse])] += 1 # if the decoded character is valid, count occurrence for once
                count2[items.index(dictionary[morse])] += 1 # if the decoded character is valid, count occurrence for once
                output = output + dictionary[morse]
            else:
                print(morse, " is invalid!")
            morse = ''
            
    # Step 3.3 : Print output only if the output exist
    if output != '' :
        print("Translated message : ", output, sep = '')
    
    if any(count2) :
        print("Occurrence for each character : ")
        for key in range(0,12) :        
            print(repr(items[key] + ':' + str(count2[key])).ljust(10),
            repr(items[key+12] + ':' + str(count2[key+12])).ljust(10),
            repr(items[key+24] + ':' + str(count2[key+24])).ljust(10))
    
    user_input = input("Please enter a sentence comprised of the 26 letters and/or 9 digits. Press Enter to quit.")

# Step 4.3 : Print Occurrence in a readable format
if any(count) :
    print("Occurrence for each character : ")
    for key in range(0,12) :        
        print(repr(items[key] + ':' + str(count[key])).ljust(10),
              repr(items[key+12] + ':' + str(count[key+12])).ljust(10),
              repr(items[key+24] + ':' + str(count[key+24])).ljust(10))
else:
    print("No valid input. No occurrence.") # if there is no valid character, which means all the counts are 0, print a message.
    
