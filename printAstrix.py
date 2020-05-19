def printAstrix(O):
    M = [['*'] * O for i in range(O)]
    for i in M:
        for j in i:
            print(j, end = ' ')
        print()

O = int(input('Please enter the number of astrix you wish to be printed: '))
printAstrix(O)
