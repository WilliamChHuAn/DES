import IO
import Box
import sys
import math
import IPFP
import keyGen
import Convert
import fFunction

def Encryption(pt, key, debug, isFromDecryption):

	# 64 bits plaintext is handed over to IP function
	pt = IPFP.initialPermutation(pt)

	if debug == True and isFromDecryption == False:
		print("After initial permutation:", Convert.binToHex(pt))
		print("Round   i      Lpt       Rpt       round keys")
		print("----------------------------------------------")

	# split plaintext into left plaintext & right plaintext
	Lpt = pt[0 : 32]
	Rpt = pt[32 : 64]

	# let the original key of 64 bits -> 56 bits by removed parity bits through PC-1 permetaion
	key = keyGen.removeParity(key)
	
	# split
	keyC = key[0 : 28]
	keyD = key[28 : 56]

	roundKey = keyGen.getRoundKeys(keyC, keyD)

	if isFromDecryption:
		roundKey = roundKey[::-1]

	'''
	16 rounds
		Li = Ri-1
		Ri = Li-1 XOR f(Ri-1, Ki)

		round key generation
			1. Spliting key into 28-bit halves (before round key generation loop)
			2. shift left 1 bit (round 1, 2, 9, 16); otherwise 2 bits
			3. Conbining and handing over to PC-2 permutation
		f-function
			1. Expanding the 32 bits data into 48 bits -> Ei
			2. Ei XOR round keyi (48 bits)
			3. Spliting into 8 S-box (each is 6 bits)
			4. S-box convert 6 bits into 4 bits
			5. Merging a 32 bits and handing over to P permutation
	'''
	for i in range(0, 16):

		Ei = fFunction.expansion(Rpt)
		afterXOR = fFunction.XOR(Ei, roundKey[i])
		aftersBox = fFunction.S(afterXOR)
		afterPermute = fFunction.permutation(aftersBox)

		# Ri = Li-1 XOR f(Ri-1, Ki)
		result = Box.XOR(Lpt, afterPermute)
		# Li = Ri-1
		Lpt = result

		# swap
		if i != 15:
			Lpt, Rpt = Rpt, Lpt

		if debug == True:
			print(f"Round {i + 1 : 3d}   {Convert.binToHex(Lpt)}   {Convert.binToHex(Rpt)}   {Convert.binToHex(roundKey[i])}")

	ct = Lpt + Rpt
	ct = IPFP.finalPermutation(ct)

	return Convert.binToHex(ct)

def Decryption(ct, key, debug):

	if debug == True:
		print("After initial permutation:", Convert.binToHex(ct))
		print("Round   i      Lct       Rct       round keys")
		print("----------------------------------------------")

	return Encryption(ct, key, debug, True)

'''
Chapter 3 Data Encryption Standard... (Class slide)

Reference about DES in Python
	https://www.ruanx.net/des/
	https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/
'''

# call IO.py for input text & key
userInput = IO.inputText(sys.argv[1:])

pt = ct = key = ""

# DES Encryption
if userInput[0] == 1:
	
	pt = Convert.hexToBin(userInput[1])
	key = Convert.hexToBin(userInput[4])
	ct = ""

	# number of blosks
	numBlock = math.ceil(len(pt) / 64)

	# initail value, end value, increment
	for i in range(0, numBlock, 1):

		# split block
		# each block of plaintext is 64 bits (padding 0)
		ptBlock = pt[i * 64 : i * 64 + 64].ljust(64, "0")

		ct += Encryption(ptBlock, key, False, False)

	IO.outputText(True, ct)

# DES Decryption
elif userInput[2] == 1:
	
	ct = Convert.hexToBin(userInput[3])
	key = Convert.hexToBin(userInput[4])
	pt = ""

	# number of blosks
	numBlock = math.ceil(len(ct) / 64)

	if len(ct) % 64 != 0:
		print("um...Are you sure?")
		sys.exit(3)

	# initail value, end value, increment
	for i in range(0, numBlock, 1):

		# split block
		ctBlock = ct[i * 64 : i * 64 + 64]

		pt += Decryption(ctBlock, key, False)

	IO.outputText(False, pt)

# maybe impossible condition if exception handling is perfect......
else:
	print("WTF!!!")
	print("Don't Hack me!!!")