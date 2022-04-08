import IO
import sys

'''
Chapter 3 Data Encryption Standard... (Class slide)

Reference about DES in Python
	https://www.ruanx.net/des/
	https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/
'''

# call IO.py for input text & key
userInput = IO.inputText(sys.argv[1:])

pt = key = ""

if userInput[0] == 1:
	print("DES Encryption")
	pt = userInput[1]
	key = userInput[4]
elif userInput[2] == 1:
	print("DES Decryption")
	ct = userInput[3]
	key = userInput[4]
# maybe impossible condition if exception handling is perfect......
else:
	print("WTF!!!")
	print("Don't Hack me!!!")