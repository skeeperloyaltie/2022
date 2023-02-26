# Accept input from the user
fName = str(input('Enter First Name: '))
lName = str(input('Enter Last Name: '))
# check if the fName and lName has characters less than 3
if len(fName) and len(lName) < 3:
    print('Not Valid \nYour first name and last name should have at least 3 characters each.')
# check if the values in the fName and lName are all numeric
elif fName.isnumeric() and lName.isnumeric() == True:
    print('Not valid name. \nYou should only use alphabets for the first name and last name.')
# if everything is valid print the names
else:
    print('Valid Name')
    print('First Name: ', fName.upper())
    print('Last Name: ', lName.upper())
