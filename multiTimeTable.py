def multiTimeTable():
    tt = int(input('Please select a number up to which timetables you would like to see (Number must be less than 10): '))
    for i in range(1, tt + 1):
        for j in range(1, 11):
            # below display the times tables 1 x 1 = 1
            # print(i, '|', i, 'x', j, '=', i*j)
            # below display the result of times tables
            print(i*j, end = ' ')
         print()

multiTimeTable()
        
    
