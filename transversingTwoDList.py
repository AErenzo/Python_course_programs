List = [[0]*3 for i in range(3)]

for i in range(len(List)):
    for j in range(len(List[i])):
        List[i][j] = int(input('Please enter a Value: '))

for i in List:
    for j in i:
        print(j, end = ' ')
    print()

