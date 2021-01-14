# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in 
the range 13..19 inclusive -- then that value counts 
as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that 
takes in an int value and returns that value fixed 
for the teen rule. In this way, you avoid repeating 
the teen code 3 times (i.e. "decomposition"). Define 
the helper below and at the same indent level as the 
main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def no_teen_sum(a, b, c):
	return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):

	count = 0
	teen = [13, 14, 17, 18, 19]

	if n not in teen:
		count += n
	count += 0

	return count

# Second Solution
def no_teen_sum(a, b, c):

	count = 0
	teen = [13, 14, 17, 18, 19]

	for num in [a, b, c]:
		if num not in teen:
			count += num
	count += 0

	return count