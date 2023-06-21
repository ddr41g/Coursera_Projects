import rsa

def load_key(key_loc):
	key=None
	with open(key_loc,'rb') as file:
		key=rsa.PrivateKey.load_pkcs1(file.read(),format='PEM')
	return key

def decrypt_file(enc_data,key):
	decrypted=rsa.decrypt(enc_data,key).decode('utf-8')
	return decrypted

def run():
	file_loc=input("Enter encrypted file location: ")
	key_loc=input("Enter key location: ")
	key=load_key(key_loc)
	with open(file_loc,'rb') as file:
		enc_data=file.read()
		dec_data=decrypt_file(enc_data,key)
	print(f"Decryption: {dec_data}")

if __name__ == '__main__':
	run()
