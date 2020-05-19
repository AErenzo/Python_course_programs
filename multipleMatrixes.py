r1 = 0
c1 = 0
r2 = 0
c2 = 0

while True:
    
    r1 = int(input('Please enter the number of rows for the first matrix: '))
    c1 = int(input('Please enter the number of columns for the first matrix: '))
    print()
    r2 = int(input('Please enter the rows for the second matrix: '))
    c2 = int(input('Please enter the columns for the second matrix: '))

    if c1 != r2:
        print('Please make sure that the column size in the first matrix matchs the row length in the second matrix.')
        continue
    else:
        break
    
# create matrix one
lOne = [[0]*c1 for i in range(r1)]

for i in range(r1):
    for j in range(c1):
        lOne[i][j] = int(input('Please enter a value for matrix one: '))
    
# create matrix two   
lTwo = [[0]*c2 for i in range(r2)]

for i in range(r2):
    for j in range(c2):
        lTwo[i][j] = int(input('Please enter a value for matrix two: '))
        
# print out matrix one 
print('Matrix one')
for i in lOne:
    for j in i:
        print(j, end = ' ')
    print()

# print out matrix two
print('Matrix two')
for i in lTwo:
    for j in i:
        print(j, end = ' ')
    print()

# create matrix three
lThree = [[0]*c2 for i in range(r1)]

# matrix multiplication logic
for i in range(r1):
    for j in range(c2):
        for k in range(r2):
            lThree[i][j] += lOne[i][k] * lTwo[k][j]
            
# print matrix 3
print('Matrix Three')
for i in lThree:
    for j in i:
        print(j, end = ' ')
    print()


