import hashlib

def checker(htype, target_hash, password):

		passwd = password
		encoded_passwd = passwd.encode('latin-1')
		final_passwd = encoded_passwd
		
		if htype == 'md5':

			hashed_passwd = hashlib.md5(final_passwd).hexdigest() 

		elif htype == 'sha1':

			hashed_passwd = hashlib.sha1(final_passwd).hexdigest()

		elif htype == 'sha256':

			hashed_passwd = hashlib.sha256(final_passwd).hexdigest()

		elif htype == 'sha512':
			
			hashed_passwd = hashlib.sha512(final_passwd).hexdigest()

		else:

			print('[-] Your hash type is not supported!')

			exit()

		if target_hash.rstrip() == hashed_passwd.rstrip():

			return True
		
		else:

			return False