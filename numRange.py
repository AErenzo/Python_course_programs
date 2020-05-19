def numRange():

    N = int(input('Please enter a number within the range of 1-10: '))

    while N < 1 or N > 10:
        print(N, 'Number not within range')
        N = int(input('Please enter another number within the range of 1-10: '))
    else:
        print('Congratulations you have selected the the correct number')
        break
        
numRange()
