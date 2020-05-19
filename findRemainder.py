def findRemainder():
    # take the value for the dividend
    dividend = int(input('Please choose the a dividend: '))
    # take the value for the divisor 
    divisor = int(input('Plase choose the divsior: '))

    # the quotient can be calculated by integer dividion (//)
    Q = dividend // divisor

    # the remainder can be calculated by the modulus operator (%)
    R = dividend % divisor

    print('Q = ', Q, '\n' 
          'R = ', R)

findRemainder()

    
