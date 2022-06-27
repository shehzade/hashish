#!/bin/python3

#Author: Abdullah Ansari

import sys, os, argparse, time
from cracker_module import checker

parser = argparse.ArgumentParser(description='Multi-Type Hash Cracking Tool')

parser.add_argument('-l', dest='_hashlist',type=str, help='Hash file path (i.e. /root/hashes.txt)')
parser.add_argument('-d', dest='_dictionary', type=str, help ='Dictionary file path (i.e. /root/rockyou.txt)')
parser.add_argument('-t', dest='_hash_type',type=str, help='Hash type [md5 | sha1 | sha256 | sha512]')

args = parser.parse_args()

hashlist = args._hashlist
dictionary = args._dictionary
hash_type = str(args._hash_type).strip()

if hash_type is None or hashlist is None or dictionary is None:

	print("\n[-] You must enter a list of hashes, a dictionary, and a hash type!")

	exit()

if os.path.exists(hashlist) and os.path.exists(dictionary):

	h = open(hashlist, 'r')
	w = open (dictionary, 'r', encoding='latin-1')

	hashes_imported = len(h.readlines())
	passwords_imported = len(w.readlines())

	print(f'\n[!] {hashes_imported} hashes and {passwords_imported} passwords have been imported!')

else:

	print('\n[-] Could not find hash/dictionary files!')

	exit()

if True:

	attempt = 0
	hash_number = 1

	print(f'\n[!] Hash mode set to: {hash_type}')
	print('\n[+] Starting dictionary attack!')

	time.sleep(1)

	print('\n[!] Attack in progress...\n')

	with open(hashlist, 'r') as working_hashes:

		for every_hash in working_hashes:

			every_hash = every_hash.strip('\n').lower()

			attempt = 0

			with open(dictionary, 'r', encoding='latin-1') as working_pass:

				for every_pass in working_pass:

					every_pass = every_pass.strip('\n')

					if checker(hash_type, every_hash, every_pass) == False:

						attempt+=1

						#print(f'\n[ATTEMPT {attempt}] [FAILURE] {every_hash}:{every_pass}')

					else:

						attempt+=1

						every_hash = every_hash.rstrip()

						print(f'[HASH#{hash_number} CRACKED] {every_hash}:{every_pass}')

						open(f'cracked_hashes.txt', 'a+').write(f'\nHash #:		{hash_number}\nType:		{hash_type}\nOriginal:	{every_hash}\nPlaintext:	{every_pass}\nAttempt #:	{attempt}\nDictionary:	{dictionary}\n')

						hash_number+=1
						
						break

	if os.path.exists('cracked_hashes.txt'):

		print('\n[+] Plaintext credentials saved to cracked_hashes.txt!')

	else:

		print('\n[-] Your dictionary did not contain the password!')
