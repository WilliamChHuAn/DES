# Data Encryption Standard (DES)

- To implement DES Algorithm in Python.

##### tags: `110-2` `Dr. Shin-Ming Cheng`

## How to use

- If you want to know how to use
	- usage: `py DES.py -h`
- If you want to ***ENCRYPT*** a message using DES Algorithm
	- usage: `py DES.py -e <plaintext> -k <8 bytes key>`
- If you want to ***DECRYPT*** a message using DES Algorithm
	- usage: `py DES.py -d <ciphertext> -k <8 bytes key>`
- This file will regard all of your input (text & key) as hexadecimal
	- i.e. key will be 16 digit

## Details

- Why only 8 bytes?
	- Because I'm lazy. I don't want to write a padding function.
- The above example command is for Windows. Please change by yourself if your environment is other OS.
	- e.g. `python3 <...>`
- Text & key are hexadecimal mean all inputs belong to 0 ~ 9A ~ F (case non-sensitive)
	- e.g. `py DES.py -e 12345678abCDEf09 -k 0123456789AbcDEF` is valid
	- e.g. `py DES.py -e 0123456789ABCDEG -k 0123456789AbcDEF` is invalid
		- Because `G` in encrypt argument isn't a hexadecimal number