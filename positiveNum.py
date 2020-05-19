def positiveNum():
    N = int(input('To keep the program running please enter a positive number: '))
    
    while N > 0:
        print(N)
        N = int(input('Please enter another positive number: '))
    else:
        print('Ooops thats a negative number')
        print('Bye for now!')
        exit
positiveNum()
    
