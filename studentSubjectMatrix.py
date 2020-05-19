students = ['maaz', 'farooq', 'maria', 'aslam']

subjects = ['math', 'physics', 'chemistry', 'biology']

matrix = [[0]*4 for i in range(4)]

total = 0

for i in range(4):
    for j in range(4):
        matrix[i][j] = int(input('Please enter student marks for the matrix: '))

for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()


# print(matrix[students.index('Farooq')][subjects.index('Biology')])

while True:

    print('-'*20)
    print('Options')
    print('1. Veiw student record for specific subject' '\n'
          '2. Find all marks for a single student' '\n'
          '3. Find total marks of a student' '\n'
          '4. Find the average marks for a single student')
    print('-'*20)

    O = int(input('Using the menu list above, please select on of the options using the index: '))


    if O == 1:
        print('Students stored in matrix', students)
        print()
        stu = (input('Using the list above please enter, exactly displayed above, the student you wish to veiw: '))
        stu.lower()
        print()
        print('Subjects stored in matrix', subjects)
        sub = (input('Please enter the subject you wish to veiw: '))
        sub.lower()
        print(matrix[students.index(stu)][subjects.index(sub)])

        break
        
    elif O == 2:
        print('Students stored in matrix')
        
        for i in students:
            print(i, end = '\n')
            
        print()
        
        stu = int(input('Input the number at which student you wish to see (1-4): '))
        
        if stu == 1:
            for i in matrix[0]:
                print(i, end = ' ')
            print()
            
        elif stu == 2:
            for i in matrix[1]:
                print(i, end = ' ')
            print()
            
        elif stu == 3:
            for i in matrix[2]:
                print(i, end = ' ')
            print()
            
        elif stu == 4:
            for i in matrix[3]:
                print(i, end = ' ')
            print()
            
        else:
            print('Invalid input')
            continue
        
              
    elif O == 3:
        print('Students stored in matrix')
        
        for i in students:
            print(i, end = '\n')    
        print()
            
        stu = int(input('Input the number at which student you wish to see (1-4): '))

        if stu == 1:
            for i in matrix[0]:
                total += i
            print('Maaz total overall score is', total)
            total = 0
                
        elif stu == 2:
            for i in matrix[1]:
                total += i
            print('farooq total overall score is', total)
            total = 0
            
        elif stu == 3:
            for i in matrix[2]:
                total += i
            print('Marias total overall score is', total)
            total = 0
                
        elif stu == 4:
            for i in matrix[3]:
                total += i
            print('Aslam total overall score is', total)
            total = 0
                
        else:
            print('Invalid input')
            continue
        
       
        
    

    elif O == 4:
        print('Students stored in matrix')
        
        for i in students:
            print(i, end = '\n')    
        print()
            
        stu = int(input('Input the number at which student you wish to see (1-4): '))

        if stu == 1:
            for i in matrix[0]:
                total += i
            avg = total // 4
            print('Maaz average score is', avg)
            total = 0
                
        elif stu == 2:
            for i in matrix[1]:
                total += i
            avg = total // 4
            print('farooq average score is', avg)
            total = 0
            
        elif stu == 3:
            for i in matrix[2]:
                total += i
            avg = total // 4
            print('Marias average score is', avg)
            total = 0
                
        elif stu == 4:
            for i in matrix[3]:
                total += i
            avg = total // 4
            print('Aslam average score is', avg)
            total = 0
                
        else:
            print('Invalid input')
            continue
        
       
    again = input('Do you want to veiw more data? (y/n): ')

    again.lower()

    if again == 'y' or 'yes':
        continue
    else:
        break
        
              
              
          
    

