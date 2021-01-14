# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a non-empty string like 
"Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def string_splosion(str):
	return ''.join([str[:idx+1] for idx in range(len(str))])

# Or

# Second Solution
def string_splosion(str):

	result = ""

	for idx in range(len(str)):
		result += str[:idx+1]

	return result