def studentResults():
    
    marks = int(input('Please enter your test score: '))

    if marks >= 70:
        
        print('Your acheived a first!')
        
    elif marks >= 60:

        print('Your passed with a 2:1')

    elif marks >= 50:

        print('You passed with a 2:2')

    else:

        print('You failed')

        

studentResults()
