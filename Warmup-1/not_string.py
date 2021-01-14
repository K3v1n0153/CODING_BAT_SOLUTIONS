# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string, return a new string where 
"not " has been added to the front. However, 
if the string already begins with "not", 
return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

########################
## SOLUTION BY: KEVIN ##
########################

def not_string(str):

	if (not 'not' == str.split()[0]):
		return 'not ' + str
	return str