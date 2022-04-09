# convert hexadecimal to binary in string type
def hexToBin(hexNumber):

	'''
	bin() return value has the prefix 0b, so use [2:]
		https://www.programiz.com/python-programming/methods/built-in/bin
	zfill() padding 0's until it reaches the specified length
		https://www.w3schools.com/python/ref_string_zfill.asp
	'''
	return bin(int(hexNumber, 16))[2:].zfill(len(hexNumber) * 4)

# convert binary to hexadecimal in string type
def binToHex(binNumber):

	'''
	hex() return value has the prefix 0x, so also use[2:]
	convert result is a lower case string, so use .upper()
		https://www.programiz.com/python-programming/methods/built-in/hex
	'''
	return hex(int(binNumber, 2))[2:].zfill(len(binNumber) // 4).upper()

# debug
def test():
	result = hexToBin("0123456789ABCDEF")
	print(result)
	print(binToHex(result))

# test()