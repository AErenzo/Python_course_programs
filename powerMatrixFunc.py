import random

# matrixSum function
def matrixSum(a, b):

    z = 'Unable to add these matrix due to their dimensions not matching'
    
    if isAdderable(a, b) ==  True:

        x = [[0] * len(a) for i in range(len(b))]
        
        for i in range(len(x)):
            for j in range(len(x)):
                x[i][j] = a[i][j] + b[i][j]
        return x
    else:
        z
# fucntion that check is the matrixes are able to be added together
def isAdderable(a, b):
    
    if len(a) == len(b):
      return True
    else:
        return False
        

# user input for the dimensions of the matrixes
n = int(input('Please eneter the dimensions of the matrixes you wish to find the sum of: '))

#create blank matrix - m1 
m1 = [[0]* n for i in range(n)]

#populate the maritix using the random fucntion
for i in range(len(m1)):
    for j in range(len(m1)):
        m1[i][j] = random.randint(1, 10)
        
#print m1 matrix
for i in m1:
    for j in i:
        print(j, end = ' ')
    print()

print()

#create blank matrix - m12    
m2 = [[0]* n for i in range(n)]

#populate the maritix using the random fucntion
for i in range(len(m2)):
    for j in range(len(m2)):
        m2[i][j] = random.randint(1, 10)

#print m2 matrix
for i in m2:
    for j in i:
        print(j, end = ' ')
    print()

#store the result of calling the matrixSum fucntion as a variable  
result = matrixSum(m1, m2)

print()

#print out the result
for i in result:
    for j in i:
        print(j, end = ' ')
    print()
