# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string, return a version without 
the first and last char, so "Hello" yields "ell".
The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""

########################
## SOLUTION BY: KEVIN ##
########################

def without_end(str):

	if len(str) >= 2:
		return str[1:-1]
	return str