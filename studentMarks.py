def studentMarks():
    
    mathScore = int(input('Please enter your math exam score: '))
    englishScore = int(input('Please enter your english exam score: '))
    scienceScore = int(input('Please enter your science exam score: '))

    average = 80

    if mathScore + englishScore + scienceScore / 3 >= average:
        print('You are above average!')
        print('Admission Granted!')

studentMarks()
