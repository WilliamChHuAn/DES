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

## Details

- Why only 8 bytes?
	- Because I'm lazy. I don't want to write a padding function.
- The above example command is for Windows. Please change by yourself if your environment is other OS.
	- e.g. `python3 <...>`
