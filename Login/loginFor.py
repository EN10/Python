print('Welcome to the login system')

for x in range(3):
    password = input('Please enter your password: ')
    if password == '1234':
        print('Welcome to the system')
        break
    else:
        print('ERROR: password not recognised')
        print(2-x , 'attempts left')
