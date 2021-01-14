# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given 2 ints, a and b, return their 
sum. However, sums in the range 10..19 
inclusive, are forbidden, so in that case 
just return 20.

sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""

########################
## SOLUTION BY: KEVIN ##
########################

def sorta_sum(a, b):

	Sum = a + b
	forbidden = list(range(10, 19+1))

	if Sum in forbidden:
		return 20
	else:
		return Sum