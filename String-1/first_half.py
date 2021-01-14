# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string of even length, return 
the first half. So the string "WooHoo" 
yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""

########################
## SOLUTION BY: KEVIN ##
########################

def first_half(str):

	str_len = len(str)

	if str_len % 2 == 0:
		return str[:int(str_len / 2)]
	else:
		return ""