def validAge():
    print('You are required to be between 18 and 24 in order to be purchase a festival ticket')
    print()

    age = int(input('Please enter your age: '))

    if age >= 18 and age <= 24:
        print('You are applicable to purchase a ticket')
    else:
        print('Sorry but you not meet the requirements to purchase a ticket')
validAge()
