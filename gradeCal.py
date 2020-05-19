def gradeCal():
    grade = int(input('Please enter your grade from the test: '))
    if grade >= 70:
        print('Your score an A+')
    elif grade >= 60:
        print('You scored an A')
    elif grade >= 50:
        print('You scored a B')
    elif grade >= 40:
        print('You socred a C')
    else:
        print('You failed')
gradeCal()
