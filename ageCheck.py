def ageCheck():
    print('We must validate your age before granting your access to this content.')
    print()
    age = int(input('Please enter your age: '))
    exp = int(input('Please enter the how many year experience you have: '))

    if age > 20 and age < 50:
        if not exp < 3:
            print('Permission granted.')
        else:
            print('Sorry you do not meet the critia to access this information.')
    else:
        print('Sorry you do not meet the critia to access this information.')

ageCheck()
