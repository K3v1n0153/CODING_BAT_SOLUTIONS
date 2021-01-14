# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given an array of ints, return the number of 9's 
in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def array_count9(nums):
	return nums.count(9)

# Or

# Second Solution
def array_count9(nums):

	count = 0

	for num in nums:
		if num == 9:
			count += 1

	return 

# Or 

# Third Solution
def array_count9(nums):

	end = len(nums)
	if end > 4:
		end = 4

	for idx in range(end):
		if nums[idx] == 9:
			return True
	return False