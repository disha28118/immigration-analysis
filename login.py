while True:
    username = input('Enter a username: ')
    password = input('Enter password: ')
    if username== 'admin' and password== 'password':
        print('Login successful')
        break
    
        print('Login failed')