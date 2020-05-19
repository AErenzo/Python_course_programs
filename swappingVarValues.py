def swappingVarValues():
    a = int(input('Please enter a value for A: '))
    b = int(input('Please enter a value for B: '))
    c = a
    a = b
    b = c
    print('A = ', a, '\n'
          'B = ', b)

swappingVarValues()
