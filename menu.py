def menu():
    print('Hello Welcome to the book shop. Please look at our menu...')
    print()
    print('1. Operating System Books' '\n'
          '2. Database Books' '\n'
          '3. Software Engineering Books' '\n')
    print()

    userOp = int(input('Using the menu displayed above, please select an options using its index number: '))

    if userOp == 1:
        print('You have selected Operating System Books')
    elif userOp == 2:
        print('You have selected Database Books')
    elif userOp == 3:
        print('You have selected Software Engineering Books')
    else:
        print('Invalid Input')
menu()
    
