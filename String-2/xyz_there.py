# Credits to: CodingBat
# Site Link: https://codingbat.com/

#############
## PROBLEM ##
#############

"""
Return True if the given string contains 
an appearance of "xyz" where the xyz is not 
directly preceeded by a period (.). So "xxyz" 
counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""

########################
## SOLUTION BY: KEVIN ##
########################

def xyz_there(str):

	if str[:3] == 'xyz':
		return True

	for idx in range(len(str)):
		if str[idx-1] != '.' and str[idx:idx+3] == 'xyz':
			return True

	return False