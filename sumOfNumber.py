def sumOfNumber():
    # user set the range which also equals the number we want to find the sum
    N = int(input('Please enter a number: '))
    # sum variable
    f = 0

    for i in range(1, N+1):
        f = f + i
        print(f)

sumOfNumber()
