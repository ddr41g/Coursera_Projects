import rsa

def load_key(key_loc):
	private_key=None
	with open(key_loc,'rb') as file:
		private_key=rsa.PrivateKey.load_pkcs1(file.read(),format='PEM')
	return private_key

def decrypt_file(enc_data,private_key):
	decrypted=rsa.decrypt(enc_data,private_key).decode('utf-8')
	return decrypted

def run():
	file_loc=input("Enter encrypted file location: ")
	key_loc=input("Enter private key location: ")
	private_key=load_key(key_loc)
	with open(file_loc,'rb') as file:
		enc_data=file.read()
		dec_data=decrypt_file(enc_data,private_key)
	print(f"Decryption: {dec_data}")

if __name__ == '__main__':
	run()
