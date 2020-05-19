import pprint

def studentMS():

    import pprint

    student = {}

    iD = 0
    firstName = ''
    secondName = ''
    rollNo = 0
    cgpa = ''
    
    while True:

        print('--------------------------''\n' # '-' * 25 will duplicate the dash 25 times
              'STUDENT MANAGEMENT SYSTEM''\n'
              '--------------------------''\n'
              '1. Add a Student''\n'
              '2. Delete a Student''\n'
              '3. Search a Student''\n'
              '4. Update a student' '\n'
              '5. Display students' '\n'
              '6. Exit/Quit')

        O = int(input('Please choose one of the option displayed in the menu: '))

      
        if O == 1:
            print()
            
            '''while True:   
                iD = input('Please enter the id of the student you wish to add: ')
                if iD in student:
                    print('This ID already exists. Please choose one which is unique')
                    continue
                else:
                    break '''

            while True:
                rollNo = input('Please enter the roll number of the student: ')
                if rollNo.isalnum():
                    break
                else:
                    print('Please enter an alphernumric number')
                    continue

            while True:
                firstName = input('Please enter the first name of the student: ')
                secondName = input('Please enter the last name of the student: ')
                if firstName.isalpha() and secondName.isalpha():
                    break
                else:
                    print('Student names must only contain alphabetical values and without a space, please try again.')
                    continue

            while True:
                try:
                    cgpa = float(input('Please enter the students cgpa: '))
                    break
                except ValueError:
                    print('Please enter integer or floating point values.')
                    continue

            iD += 1
            student.update({iD: {'Name':firstName +' '+ secondName, 'Roll Number':rollNo, 'cgpa':float(cgpa)}})
            print('Student record updated successfully', iD, firstName + ' ' + secondName, rollNo, float(cgpa))   
            

            
           
            
            
        elif O == 2:
            print()
            iD = input('Please enter the id of the student you wish to remove: ')
            result = student.get(iD, -1)
            if result == -1:
                print('Sorry student no found in database')
            else:
                del student[iD]
                print('Student deleted')
            
        elif O == 3:
            print()
            iD = input('Please enter the id of the student you wish to search: ')
            print('Searching...')
            
            result = student.get(iD, -1)
            
            if result == -1:
                print('Sorry student not found for id', iD)
            else:
                pprint.pprint(student[iD])
                

        elif O == 4:
            print()
            iD = input('Please enter the id of the student you wish to update: ')

            result = student.get(iD, -1)
            
            if result == -1:
                print('student not found at id', iD)
            else:
                print()
                print('Update options''\n'
                      '1. Update student name''\n'
                      '2. Update student roll number''\n'
                      '3. Update student cgpa''\n'
                      '4. update all')
                print()
                update = int(input('Please choose one of the options above for updating student records: '))
                print()    
                if update == 1:
                    
                    while True:
                        print('1. First name' '\n'
                                '2. Second name' '\n'
                                '3. Full name' '\n')
                        print()
                        
                        O = int(input('Please choose one of the options above to update a students name: '))
                        
                        if O == 1:
                            firstName = input('Please enter the students updated first name: ')
                            student[iD]['Name'] = firstName + ' ' + secondName
                            print('Students name updated successfully', student[iD])
                            break

                        elif O == 2:
                            secondName = input('Please enter the students updated second name: ')
                            student[iD]['Name'] = firstName + ' ' + secondName
                            print('Students second name updated successfully', student[iD])
                            break

                        elif O == 3:
                            firstName = input('Please enter the students updated first name: ')
                            secondName = input('Please enter the students updated second name: ')
                            student[iD]['Name'] = firstName + ' ' + secondName
                            print('Students full name updated successfully', student[iD])
                            break

                        else:
                            print('Invalid option, please choose one of the options above')
                            continue

                elif update == 2:
                    rollNo = input('Please enter the students new roll number: ')
                    student[iD]['Roll Number'] = rollNo
                    print('Roll number updated successfully', student[iD])

                elif update == 3:
                    cgpa = float(input('Please enter students new cgpa: '))
                    student[iD]['cgpa'] = float(cgpa)
                    print('Students cgpa has been updated successfully', student[iD])

                elif update == 4:
                    firstName = input('Please enter the students updated first name: ')
                    secondName = input('Please enter the students updated second name: ')
                    rollNo = input('Please enter the students new roll number: ')
                    cgpa = input('Please enter students new cgpa: ')
                    student.update({iD: {'Name':firstName +' '+ secondName, 'Roll Number':rollNo, 'cgpa':float(cgpa)}})
                    print(student[iD])
                    
            
        elif O == 5:
            print(pprint.pprint(student))
            
        elif O == 6:
            print('Exiting...')
            break
        else:
            print('Invalid input')

            
        c = input('Would you like to try again?(y/n): ')


        if C.islower() == 'n':
            break
        else:
            continue

    print('Closing Down')

studentMS()

    
