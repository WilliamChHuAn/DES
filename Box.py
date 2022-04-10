# rearrange the bits
def permute(text, table, length):

	result = ""
	
	'''
	table[new position] = old position, so use string concatenate to append (new element is from 0 to 63)
		table[index] -> index from 1 to 64, so table[i] - 1
	'''
	for i in range(0, length):
		result = result + text[table[i] - 1]
	
	return result

def XOR(L, fR):
	
	result = ""
	
	for i in range(len(L)):
		if L[i] == fR[i]:
			result += "0"
		else:
			result += "1"

	return result