# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Return the number of times that the
string "hi" appears anywhere in the 
given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def count_hi(str):
	return str.count('hi')

# Or

# Second Solution
def count_hi(str):

	return sum(1 for idx in range(len(str)-1)
			if str[idx] == 'h' and str[idx+1] == 'i'
		)