# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Return the number of times that the 
string "code" appears anywhere in the 
given string, except we'll accept any letter 
for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Soluton
def count_code(str):

	count_valid = 0
	valid_string = ('code', 'coze', 'cope', 'cole', 'core')

	for vs in valid_string:
		count_valid += str.count(vs)
			
	return count_valid

# Or

# Second Solution
def count_code(str):
	return sum(1 for idx in range(len(str)-3)
		if str[idx:idx+2] == 'co' and str[idx+3] == 'e'
	)