# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Return True if the string "cat" and 
"dog" appear the same number of times 
in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

########################
## SOLUTION BY: KEVIN ##
########################

# First Solution
def cat_dog(str):

	cat_count = 0
	dog_count = 0

	if len(str) == 3:
		return False
	else:
		if 'cat' in str:
			cat_count += str.count('cat')
			if 'dog' in str:
				dog_count += str.count('dog')
			else:
				return False
		else:
			return True

	return cat_count == dog_count

# Or

# Second Solution
def cat_dog(str):

	cat_count = str.count('cat')
	dog_count = str.count('dog')

	return cat_count == dog_count