# python
# Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function.
# Complete the test to produce the perfect function that accounts for all expectations.

# For strings, return its length.
# For None return string 'no value'
# For booleans return the boolean
# For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
# For lists return the 3rd item, or None if it doesn't exist

n = False

def data_types(n):
	if (type(n) == type("")):
 		return len(n)
	elif(type(n) == type(None)):
		return 'no value'

	elif(type(n) == type(False)):
		return  n

	elif (type(n) == type(3)):

		if (n < 100 ):
			return "less than 100"
		elif (n > 100):
			return "more than 100"	
		
		else:
		    return "more than 100"

	elif (type(n) == type([])):

		if len[n] >= 3:
		
			return [2]
		else:
			return "None"
print (data_types(n))
