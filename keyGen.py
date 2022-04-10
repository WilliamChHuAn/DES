import Box

# let the 64-bit key change into 56-bit key (removing parity of each byte)
pc1 = [57, 49, 41, 33, 25, 17,  9,
		1, 58, 50, 42, 34, 26, 18,
	   10,  2, 59, 51, 43, 35, 27,
	   19, 11,  3, 60, 52, 44, 36,
	   63, 55, 47, 39, 31, 23, 15,
		7, 62, 54, 46, 38, 30, 22,
	   14,  6, 61, 53, 45, 37, 29,
	   21, 13,  5, 28, 20, 12,  4]

# let the 56-bit key change into 48-bit round key
pc2 = [14, 17, 11, 24,  1,  5,
		3, 28, 15,  6, 21, 10,
	   23, 19, 12,  4, 26,  8,
	   16,  7, 27, 20, 13,  2,
	   41, 52, 31, 37, 47, 55,
	   30, 40, 51, 45, 33, 48,
	   44, 49, 39, 56, 34, 53,
	   46, 42, 50, 36, 29, 32]

# In rounds 𝑖 = 1, 2, 9, 16, the two halves are each rotated left by one bit
# In all other rounds where the two halves are each rotated left by two bits
shiftTimes = [1, 1, 2, 2,
			  2, 2, 2, 2,
			  1, 2, 2, 2,
			  2, 2, 2, 1]

def removeParity(key):
	return Box.permute(key, pc1, len(pc1))

def shiftLeft(key, roundI):

	for i in range(shiftTimes[roundI]):

		result = ""

		for j in range(1, len(key)):
			result += key[j]

		# rotate
		result += key[0]
		key = result

	return key

def permutation(key):
	return Box.permute(key, pc2, len(pc2))

def getRoundKeys(keyC, keyD):

	roundKey = []

	for i in range(0, 16):

		# conbine and shift
		keyC = shiftLeft(keyC, i)
		keyD = shiftLeft(keyD, i)
		
		# permute
		roundKey.append(permutation(keyC + keyD))

	return roundKey