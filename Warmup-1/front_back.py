# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string, return a new string where the first 
and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

########################
## SOLUTION BY: KEVIN ##
########################

def front_back(str):
	if len(str) > 1:
		return str[-1] + str[1:-1] + str[0]
	return str