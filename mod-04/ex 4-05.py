user = 'python'
passwd = 'rules'
tries = 0
while tries < 5:
    username = input('Enter the username: ')
    password = input('Enter the password: ')
    if username == user and password == passwd:
        print('Welcome')
        break
    else:
        print('Incorrect credentials, try again')
        tries += 1
if tries > 5:
    print('Access denied')