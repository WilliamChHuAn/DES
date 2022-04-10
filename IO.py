# Input / Output

import os, sys, getopt

'''
References about error handling & cmd argument parser：
	https://docs.python.org/3/tutorial/errors.html
	https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
'''

# User-defined exceptions for option & argument error or help message
class helpError(Exception):
	
	useHelp = '''-------------------------------------------------------------------------
| Please check README or use the command below                          |
| usage: py DES.py -h                                                   |
-------------------------------------------------------------------------
'''
	
	helpMessage = '''-------------------------------------------------------------------------
| If you want to ENCRYPT a message using DES Algorithm                  |
| usage: py DES.py -e <plaintext> -k <8 bytes key>                      |
|                                                                       |
| If you want to DECRYPT a message using DES Algorithm                  |
| usage: py DES.py -d <ciphertext> -k <8 bytes key>                     |
|                                                                       |
| This file will regard all of your input (text & key) as hexadecimal   |
| i.e. key will be 16 digits                                            |
|                                                                       |
| If this message still alert, you can open README.md for more details  |
-------------------------------------------------------------------------
'''

# input plaintext or ciphertext that users want to encrypt or decrypt
def inputText(argv):

	e = d = 0
	pt = ct = key = ""

	# get options (encrypt or decrypt) & arguments (text & key)
	try:
		optsArgs, useless = getopt.getopt(argv, "he:d:k:", ["help=", "encrypt=", "decrypt=", "key="])
	
		# optsArgs is a list of (option, argument) pairs
		for opt, arg in optsArgs:
		 	if opt == "-h":
		 		raise helpError
		 	elif opt in ("-e", "--encrypt"):
		 		e = 1
		 		pt = arg
		 	elif opt in ("-d", "--decrypt"):
		 		d = 1
		 		ct = arg
		 	elif opt in ("-k", "--key"):
		 		key = arg

		# convert all letters to upper case
		key = key.upper()
		textKey = [e, pt, d, ct, key]

		# when e == True or d == True but e != d, and key was entered
		if (e ^ d) and len(key) == 16:
			for i in key:
				if i not in "0123456789ABCDEF":
					raise helpError
			return textKey
		else:
			raise helpError

	# unrecognized option or option requiring an argument is given none
	except getopt.GetoptError:
		print()
		print(helpError.useHelp)
		os._exit(1)
	
	# let user know how to use
	except helpError:
		print()
		print(helpError.helpMessage)
		os._exit(2)

# output the encrypt or decrypt result
# if flag == True represent it's encryption; otherwise it's decryption
def outputText(flag, text):
	print()
	if flag == True:
		print("After DES encrypt")
		print("-----------------")
		print("Ciphertext: ", end = "")
	else:
		print("After DES decrypt")
		print("-----------------")
		print("Plaintext: ", end = "")
	print(text)

# debug
def test():
	inputText(sys.argv[1:])

# test()