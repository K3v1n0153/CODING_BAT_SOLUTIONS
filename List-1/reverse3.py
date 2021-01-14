# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given an array of ints length 3, return 
a new array with the elements in reverse 
order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def reverse3(nums):
	return nums[::-1]

# Or

def reverse3(nums):

	result = []

	for idx in range(len(nums)-1, -1, -1):
		result.append(nums[idx])

	return result