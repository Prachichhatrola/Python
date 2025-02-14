username = input('Username: ')
password = input('Password: ')
hiddenpass = '*' * len(password)

print(f'{username}, your password {hiddenpass} is {len(password)} letters long')
