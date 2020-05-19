def highNumber():
    
    print('Hello in this program, i will determine the highest number based on your input: ')

    a = int(input('Please enter the first number: '))
    b = int(input('Please eneter the second number: '))
    c = int(input('Please enter the third number: '))

    if a > b and a > c:
       print(a, 'is the highest number.')
       
    elif b > a and b > c:
        print(b, 'is the highest number.')

    elif c > a and c > b:
        print(c, 'is the highest number.')

    else:
        print('All number are of the same value')

highNumber()
