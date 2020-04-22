def encrypt(cipher):
	#creates a function called encrypt which has a parameter called cipher. 
	encrypt=[]
	for i in cipher:
		encrypt.append(chr(ord(i)+5))
	#iterates through each character in the ciper and encrypts it.
	#for the encryption I converted each character to ASCII, added 5 to the value and then converted back to a character.	
	encrypted=''.join(encrypt)
	return encrypted
	#joins the encrypted charcters and then returns the string.

def decrypt(cipher):
	#creates a function called decrypt which has a parameter called cipher.	
	decrypt =[]
	for i in cipher:
		decrypt.append(chr(ord(i)-5))
	#iterates through each character in the ciper and decrypts it by subtracting 5 from the ASCII value.
	decrypted=''.join(decrypt)
	return decrypted	
	#joins the decrypted characters together to make the decrypted string and then returns it.

