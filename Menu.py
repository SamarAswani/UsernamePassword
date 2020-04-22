def menu():
	print("""Please choose a menu option:
    1: Create Account
    2: Log In
    3: Quit

    :          """)

    #Displays menu

	while True:
		try:
			user_input = int(input())
			break
		except ValueError:
			print("You have not entered a number, please try again")
    #This is an example of exception handling. If the user does not enter a number an error is thrown.
    #This means that if an error occurs then the program doesn't crash and the user can continue to enter
    #another input.    
	while user_input > 3 or user_input < 1:
		try:
			user_input = int(input("Please enter a valid menu option "))
		except ValueError:
			print("You have not entered a number, please try again")
	#The same form of exception handling is used here.
	#However, it also checks that the number entered is a menu option (between 1-3).		
			
	return(user_input)    #returns user input