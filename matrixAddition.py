r1 = int(input('Please enter the number of rows for the first matrix: '))
c1 = int(input('Please enter the number of columns for the first matrix: '))

List_one = [[0]*c1  for i in range(r1)]

for i in range(len(List_one)):
    for j in range(len(List_one[i])):
        List_one[i][j] = int(input('Please enter a value for the first list: '))
print()
print(List_one)

r2 = int(input('Please enter the rows for the second matrix: '))
c2 = int(input('Please enter the columns for the second matrix: '))

List_two = [[0]*c2 for i in range(r2)]

for i in range(len(List_two)):
    for j in range(len(List_two[i])):
        List_two[i][j] = int(input('Please enter a value for the second list: '))

print()
print(List_two)

List_three = [[0]*3 for i in range(3)]

for i in range(len(List_three)):
    for j in range(len(List_three[i])):
        List_three[i][j] = List_one[i][j] + List_two[i][j]

for i in List_three:
    for j in i:
        print(j, end = ' ')
    print()
