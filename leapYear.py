def leapYear():
    print('In this program we will determine if the year is a leap year or not')

    year = int(input('Please enter the year: '))

    if year % 4 == 0:
        
        if year % 100 == 0:
            
            if year % 400 == 0:
                print('if is a leap year!')
            else:
                print('It is a normal year')
                
        else:
            print('It is a leap year')
            
    else:
        print('It is a normal year')

leapYear()
