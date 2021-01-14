# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string, return the count of the 
number of times that a substring length 2 
appears in the string and also as the last 2 
chars of the string, so "hixxxhi" yields 1 
(we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def last2(str):

	if len(str) < 2:
		result = 0
	else:
		result = len([1 for idx in range(len(str)-2) if str[idx:idx+2] == str[-2:]])

	return result

# Or

# Second Solution
def last2(str):

	if len(str) < 2:
		return 0

	last_2 = str[-2:]
	count = 0

	for idx in range(len(str)-2):

		sub = str[idx:idx+2]

		if sub == last_2:
			count += 1

	return count