# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given an array of ints, return True if the sequence
 of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

########################
## SOLUTION BY: KEVIN ##
########################

def array123(nums):

	for idx in range(len(nums)-2):
		if nums[idx] == 1 and nums[idx+1] == 2 and nums[idx+2] == 3:
			return True
	return False