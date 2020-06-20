print('Welcome to the login system')
f = open("password.txt", "r")
storedpassword = f.read()

for x in range(3):
    inputpassword = input('Please enter your password: ') + "\n"
    if inputpassword == storedpassword:
        print('Welcome to the system')
        ans = input('Change Password? y/n ')
        if ans == 'y':
            NewPassword = input('New Password? ')
            f = open("password.txt", "w")
            f.write(NewPassword)
            f.close()
        break
    else:
        print('ERROR: password not recognised')
        print(2-x , 'attempts left')
