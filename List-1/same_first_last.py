# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given an array of ints, return True if 
the array is length 1 or more, and the 
first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""

########################
## SOLUTION BY: KEVIN ##
########################

def same_first_last(nums):

	if (len(nums) >= 1) and (nums[0] == nums[-1]):
		return True
	return False