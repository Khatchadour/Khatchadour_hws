import re

while True:
    password = input('Password: ')
    if len(password) < 8:
        print('Make sure your password has at least 8 letters')
    elif re.search(r"[0-9]", password) is None:
        print('Make sure your password has a number in it')
    elif re.search(r"[A-Z]", password) is None:
        print('Make sure your password has a capital letter in it')
    else:
        print('Welcome!')
        break