import sys
from Quit import quit
from Menu import menu
from CreateAccount import create_account
from LogIn import login
from encryption import encrypt
from encryption import decrypt
#importing all the functions from my programs.

while True:
	user_input = menu()
	#runs the menu function and stores the returned user input in a variable.

	if user_input ==1:
		create_account()
#if user input is 1 then the create account function is called.

	elif user_input ==2:
		login()
#if user input is 2 then the log in function is called.
	
	elif user_input ==3:
		quit()		

#if the uesr input is 3 then the quit function is called.