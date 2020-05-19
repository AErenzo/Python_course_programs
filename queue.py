from collections import deque


queue = deque([])


while True:
    print('--------------------------''\n' # '-' * 25 will duplicate the dash 25 times
            'STACK MANAGEMENT SYSTEM''\n'
            '--------------------------''\n'
            '1. Insert element''\n'
            '2. Delete element''\n'
            '3. Display stack' '\n'
            '4. Exit/Quit')

    print()
    O = int(input('Please select one of the options diplayed above, using its index number: '))
    
    if O == 1:
        if len(queue) < 5:
            print()
            element = input('Please enter the element you wish to add: ')
            queue.append(element)
            print()
            print('The element', element, 'has been added to the stack')
        else:
            print()
            print('Sorry, your queue is already full')

    elif O == 2:
        if len(queue) > 0:
            rElement = queue.popleft()
            print()
            print('First element of the queue has been removed:', rElement)
        else:
            print()
            print('Queue is already empty')

    elif O == 3:
        for i in queue:
            print(i, end = '\n')
        print()

    elif O ==  4:
        print()
        print('Exiting program')
        break

    else:
        print()
        print('Invlaid input, please choose an option from the menu, using the menu index.')

   # more = input('Do you want to continue? ')

   # if more == 'y' or more == 'Y':
  #      continue
   # else:
  #      print()
   #     print('Exiting program')
    #    break
