import string

def decrypt_ciphertext(ciphertext,key):
	plaintext=''

	for c in ciphertext:
		if c.isupper():
			alphabet=string.ascii_uppercase
		elif c.islower():
			alphabet=string.ascii_lowercase
		else:
			plaintext+=c
			continue
		
		position=alphabet.find(c)
		shift_position=(position-int(key))%26
		plainletter=alphabet[shift_position]
		plaintext+=plainletter

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
	key=input("Enter the key: ")
	print("Decrypted text:",decrypt_ciphertext(ciphertext,key))



if __name__ == '__main__':
	run()
