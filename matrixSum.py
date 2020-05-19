# Take input for matrix dimensions
c = int(input('Set dimensions of your 2d list. Enter a number (NxN): '))

# set dimensions on matrix based off user input - creating matrix
matrix = [[0]*c for i in range(c)]

# loop through our empty matrix and get user input to populate
for i in range(c):
    for j in range(c):
        matrix[i][j] = int(input('Please enter a nuumber for the matrix: '))

# print matrix
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

# set total var 
total = 0

# for loop count the sum of each row
for i in range(len(matrix)):
    for j in range(len(matrix)):
        total = total + matrix[i][j]
    # add the sum of row stored at total, on the end of matrix[i]    
    matrix[i].append(total)
    print(matrix[i])
    # reset total
    total = 0
    

# blank list for column sums        
col = []

# for loop count the sum of each column
for i in range(len(matrix)):
    for j in range(len(matrix)):
        total += matrix[j][i]
    # add the total into the col blank list
    col.append(total)
    total = 0
   
# once all column sums have been added to col, append the list onto the matrix
# so it appear at the bottom
matrix.append(col)


# print matrix
print()
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()
