'''p
u'''


while True:
    U = input('Please enter your username: ')

    if U.isalnum():
        break
    else:
        print('Username must consist of alphanumeric values')

while True:
    P = input('Please enter your password: ')
    if P.isnumeric() and len(P) < 11:
        break
    else:
        print('Incorrect password. Maximum length is 10 and must contain numbers only')

print('Access Granted')
