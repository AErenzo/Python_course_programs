def basicCal():
    firstNo = float(input('Please choose a number: '))
    secondNo = float(input('Please choose a number: '))
    oporater = input('Please select an oporator, your options are +, -, / or *: ')

    if oporater == '+':
        print(firstNo + secondNo)
        
    elif oporater == '-':
        print(firstNo - secondNo)
        
    elif oporater == '/':
        if secondNo == 0:
            print('Error: Divisor cant be zero')
        else:
            print(firstNo / secondNo)
        
    elif oporater == '*':
        print(firstNo * secondNo)
        
    else:
        print('Invalid Input')
        
basicCal()
        








    

