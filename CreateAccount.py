from encryption import encrypt
from encryption import decrypt

def create_account():
	#creates function called create_account.
	common_passwords=[]

	with open ("common_passwords.txt",'r') as common_pass:
		common_passwords = common_pass.read().split(' ')
		#opens the common passwords text file and then splits it into an array, where each variable is
		#a common password.
	taken_usernames = []

	with open ("file.txt") as username_check:
		for line in username_check:
			information = line.split()
			taken_usernames.append(decrypt(information[0]))
	#opens the text file with all the usernames and passwords.
	#this code then splits the username and password into 2 variables in the array 'information'.
	#the first variable (which is the username) is then decrypted using the decryption function and appended to the taken usernames array.		
	
	username = input("Please enter a username that is between 6-20 characters in length and has no spaces: \n")
	
	while len(username)<6 or len(username)>20 or ' ' in username or username in taken_usernames:
		if username in taken_usernames:
			print("that username is already taken")
		username = input("please enter a username that is between 6-20 characters in length and has no spaces: \n")
	#This loop checks and makes sure that the username that the user enters has no spaces, is not taken and also is between 6 and 20 characters long.
		
	num, upper_case, lower_case =0,0,0
    
	while num<=0 or upper_case <= 0 or lower_case <=0 or len(password)>20 or len(password)<8 or ' ' in password or password in common_passwords:
		num, upper_case, lower_case =0,0,0
		password = input ("Please enter a password that is 8-20 and contains the following requirements: \nNo spaces \nAtleast 1 Uppercase character \nAtleast 1 Lowercase character\nAtleast 1 number : \n")    
		for i in password:
			if i.isdigit():
				num+=1
			elif i == i.upper():
				upper_case+=1
			elif i == i.lower():
				lower_case+=1
		
		if ' ' in password:
			print("Password must contain no spaces \n")
		if password in common_passwords:
			print("This password is a common password \n")
		
		#This embedded for loop iterates through every character in the password and checks if it is an uppercase letter, lowercase letter or a number.
		#It then counts the number of uppercase letters, lowercase letters and numbers.
		#The while loop makes sure that there is atleast one uppercase letter, one lowercase letter and one number.
		#It also makes sure that the password is between 6 and 20 characters, has no spaces and is not a common password.

	print("\nYour account has been created. You can now log in. \n")

	username = encrypt(username)
	password = encrypt(password)				
	#Encrypts username and password using the encryption function I created.

	with open("file.txt", "a") as myfile:
		myfile.write(username + ' ' + password+"\n")

	#Stores encrypted username and password in text file	



