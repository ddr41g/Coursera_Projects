from cryptography.fernet import Fernet

def load_key(key_loc):
	key=open(key_loc,'rb').read()
	return key

def decrypt_file(file_loc,key):
	f = Fernet(key)
	with open(file_loc,'rb') as file:
		enc_data=file.read()
	dec_data=f.decrypt(enc_data)

	with open("./fernet_decrypted.txt",'wb') as file:
		file.write(dec_data)

def run():
	file_loc=input("Enter encrypted file location: ")
	key_loc=input("Enter key location: ")
	key=load_key(key_loc)
	decrypt_file(file_loc,key)
	print("File 'fernet_decrypted.txt' created")

if __name__ == '__main__':
	run()
