# -*- coding: utf-8 -*-
"""
Task 1

In this task, I made a dictionary to store Morse Code table. 
The keys of the dictionary are the Morse Code in binary digits format. 
And the values of the keys are the standard 26 letters and the 10 numerals. 
Then I used repr() in print() to make the output dictionary readable.

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

# Step 1.4: Print dictionary in a readable format
for key in range(0,12) :        
    print(repr(dictionary[list(dictionary.keys())[key]] + ':' + list(dictionary.keys())[key]).ljust(10),
          repr(dictionary[list(dictionary.keys())[key+12]] + ':' + list(dictionary.keys())[key+12]).ljust(10),
          repr(dictionary[list(dictionary.keys())[key+24]] + ':' + list(dictionary.keys())[key+24]).ljust(10))