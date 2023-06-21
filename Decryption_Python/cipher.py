def decrypt_ciphertext(ciphertext):
	plaintext=ciphertext.replace(";","")
	return plaintext


def run():
	ciphertext = input("Enter the ciphertext: ")
	choice = input(f"Do you want to decrypt the following text {ciphertext}? Enter (y/n): ")

	if choice == 'y':
		plaintext = decrypt_ciphertext(ciphertext)
		print("Successful")
		print(f"Original Plaintext Message: {plaintext}")

	else:
		print("Goodbye")


if __name__ == '__main__':
	run()
