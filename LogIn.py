import sys
from encryption import decrypt
from CreateAccount import create_account
def login():
	#Creates function called login.
	usernames_passwords = {}
	#username and password dictionary is created.
	with open ("file.txt") as checkInfo:
		for line in checkInfo:
			#loops through each line in the text file.
			information = line.split()
			#splits the username and password in each line into 2 seperate variables and stores it in the information array.
			user = decrypt(information[0])
			passw = decrypt(information[1])
			#the username and password in the text file are decrypted using the decrypting function and then assigned to their respective variables.
			key, val = user, passw
			usernames_passwords [key] = val
			#stores the username and password in a dictionary where the username is the key and password is the value.

	username_input = input("enter your username: \n")
	
	try:
		corr_password = usernames_passwords[username_input]
		#if the user enters a valid username the correct password for that username is stored in this variable.
	except KeyError:
		#if the username is not valid this prevents an error from being thrown.
		print("This is not a valid username \n")
		print("If you do not have an account you can create one")
		create_account()
		#calls the create account function if the username is not valid so the user can create an account.
		return
		#once the new account is created this function ends due to this return.


	password_input = input("enter your password: \n")

	if password_input == corr_password:
		print("you have been successfully logged in \n")
		#checks if the password inputted is correct for that username.

	else:
		print("this password is incorrect. You have 3 more tries")
		for i in range (0,3):
			password_input = input("enter your password: \n")
			if password_input == corr_password:
				print("You have successfully been logged in \n")
				break
			else:
				print("This password is incorrect. You have",2-i,"more tries")	
		#gives the user 3 more tries to enter the password.		

		sys.exit()
		#exits program if the user does not get the password in 3 tries
