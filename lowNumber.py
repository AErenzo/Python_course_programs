def lowNumber():
    print('Hello is this program we will determine the smallest number from the user input')
    print()

    a = int(input('Please enter number A: '))
    b = int(input('Please enter number B: '))
    c = int(input('Please enter number C: '))

    if a < b:
        if a < c:
            print(a, 'is the smallest number')
        else:
            print(c, 'is the smallest number')
    else:
        if b < c:
            print(b, 'is the smallest number')
        else:
            print(c, 'is the smallest number')
lowNumber()
