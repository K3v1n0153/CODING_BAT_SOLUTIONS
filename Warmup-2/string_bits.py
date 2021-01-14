# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string, return a new string 
made of every other char starting with 
the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

########################
## SOLUTION BY: KEVIN ##
########################

string = 'Heeololeo'

new_string = ""
for idx in range(0,len(string), 2):
	new_string += string[idx]

print(new_string)

# First Solution
def string_bits(str):

	result = ""
	for idx in range(len(str), 2):
		result += str[idx]

	return result

# Or

# Second Soluton
def string_bits(str):

	result = ""

	for idx in range(len(str)):

		if idx % 2 == 0:
			result += str[idx]

	return result