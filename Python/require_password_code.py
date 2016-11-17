import getpass

p=str("null")    # user's input start value
pas=str("password") # password value
while p!=pas:
	p=getpass.getpass("Enter your password: ")     # password input
print("Password was correct!")    # when you get the password, this is the output
