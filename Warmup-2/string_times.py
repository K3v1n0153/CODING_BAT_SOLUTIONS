# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given a string and a non-negative int n, 
return a larger string that is n copies 
of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def string_times(str, n):
	return str*n

# Or

# Second Solution
def string_times(str, n):

	result = ""

	for n in range(n):
		result += str

	return result