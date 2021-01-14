# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given an array of ints, return True 
if the array contains a 2 next to a 2 
somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""

########################
## SOLUTION BY: KEVIN ##
########################

def has22(nums):

	for idx in range(len(nums)-1):
		if nums[idx] == 2 and nums[idx+1] == 2:
			return True
	return False