# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string, return a string where 
for every char in the original, there 
are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""

########################
## SOLUTION BY: KEVIN ##
########################

def double_char(str):

	return ''.join([letter*2 for letter in str])