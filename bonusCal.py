def bonusCal():
    print('Hello were are here to determine your bonus.')
    print()
    salary = int(input('Please enter your salary: '))
    grade = int(input('Please enter your grade: '))
    if grade > 15:
        print('Next years salary: ',salary * 1.5)
    else:
        print('Next years salary: ',salary * 1.25)
bonusCal()
