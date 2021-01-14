# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Return the sum of the numbers in the array, 
returning 0 for an empty array. Except the 
number 13 is very unlucky, so it does not 
count and numbers that come immediately after 
a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""

########################
## SOLUTION BY: KEVIN ##
########################

def sum13(nums):

	sum = 0

	if len(nums) > 0 and nums[0] != 13:
		sum = nums[0]

	for idx in range(1, len(nums)):

		if nums[idx] != 13 and nums[idx-1] != 13:
			sum += nums[idx]

	return sum