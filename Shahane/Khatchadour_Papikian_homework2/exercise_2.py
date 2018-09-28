while True:
    username = input('username: ')
    password = input('password: ')
    if username == 'Batman' and password == 'I am Batman':
        print('Welcome!')
        break
    else: print('incorrect USERNAME or PASSWORD')