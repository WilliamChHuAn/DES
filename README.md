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

- Key must be exactly 8 bytes 16 digits!!!
	- Because I'm lazy. I don't want to write a padding function.
- The above example command is for Windows. Please change by yourself if your environment is other OS.
	- e.g. `python3 <...>`
- Text & key are both hexadecimal numbers mean all inputs must belong to 0 ~ 9A ~ F (case non-sensitive)
	- e.g. `py DES.py -e 12345678abCDEf09 -k 0123456789AbcDEF` is valid
	- e.g. `py DES.py -e 0123456789ABCDEG -k 0123456789AbcDEF` is invalid
		- Because `G` in encrypt argument isn't a hexadecimal number
- **ECB** mode & **Zero padding**
	- This online tool can choose ECB & Zero padding, thus you can double check the result is correct or not
		- https://the-x.cn/en-US/cryptography/Des.aspx

## Example

- You can modify the Encryption() or Decryption() 3rd argument to debug and see the below result
- Encryption
	- Plaintext: `0123456789ABCDEF`
	- Key: `0123456789ABCDEF`
	```
	After initial permutation: CC00CCFFF0AAF0AA
	Round   i      Lpt       Rpt       round keys
	----------------------------------------------
	Round   1   F0AAF0AA   5E1CEC63   0B02679B49A5
	Round   2   5E1CEC63   82E13C49   69A659256A26
	Round   3   82E13C49   499542F9   45D48AB428D2
	Round   4   499542F9   0DD64AFB   7289D2A58257
	Round   5   0DD64AFB   7036043B   3CE80317A6C2
	Round   6   7036043B   F1470BC2   23251E3C8545
	Round   7   F1470BC2   394C8F45   6C04950AE4C6
	Round   8   394C8F45   348DC746   5788386CE581
	Round   9   348DC746   F37100C6   C0C9E926B839
	Round  10   F37100C6   3C22A9CB   91E307631D72
	Round  11   3C22A9CB   0A37C369   211F830D893A
	Round  12   0A37C369   5C725FFB   7130E5455C54
	Round  13   5C725FFB   F4748AD6   91C4D04980FC
	Round  14   F4748AD6   CC6C340E   5443B681DC8D
	Round  15   CC6C340E   BA88F699   B691050A16B5
	Round  16   FB21FB9C   BA88F699   CA3D03B87032

	After DES encrypt
	-----------------
	Ciphertext: 56CC09E7CFDC4CEF
	```
