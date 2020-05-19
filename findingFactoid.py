def findingFactoid():
    factoid = int(input('Please enter the number you wish to find the factoid of: '))

    f = 1

    for i in range(1, factoid+1):
        f = f * i
        print(f, end = ', ')
findingFactoid()
