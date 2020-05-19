stack = []

while True:
    print('--------------------------''\n' # '-' * 25 will duplicate the dash 25 times
            'STACK MANAGEMENT SYSTEM''\n'
            '--------------------------''\n'
            '1. Insert element in stack''\n'
            '2. Delete element from stack''\n'
            '3. Display stack' '\n'
            '4. Exit/Quit')

    print()
    O = int(input('Please select one of the options diplayed above, using its index number: '))
    
    if O == 1:
        if len(stack) < 5:
            print()
            element = input('Please enter the element you wish to add: ')
            stack.append(element)
            print()
            print('The element', element, 'has been added to the stack')
        else:
            print()
            print('Sorry, your stack is already full')

    elif O == 2:
        if len(stack) > 0:
            rElement = stack.pop()
            print()
            print('Last element of the stack has been removed:', rElement)
        else:
            print()
            print('Stack is already empty')

    elif O == 3:
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

    elif O ==  4:
        print()
        print('Exiting program')
        break

    else:
        print()
        print('Invlaid input, please choose an option from the menu, using the menu index.')

    more = input('Do you want to continue? ')

    if more == 'y' or more == 'Y':
        continue
    else:
        print()
        print('Exiting program')
        break
