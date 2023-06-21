def decrypt_ciphertext(ciphertext):
	plaintext=reverse_text(ciphertext)
	return plaintext

def reverse_text(message):
	reversed=''
	i=len(message)-1
	while i >=0:
		reversed+=message[i]
		i-=1
	return reversed

def run():
	ciphertext = input("Enter the ciphertext: ")
	print("Decrypted text:",decrypt_ciphertext(ciphertext))

if __name__ == '__main__':
	run()
