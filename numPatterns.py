List = []
Sum = 0

for i in range(5):
    item = int(input('What would you like to add to your list? '))
    List.append(item)

    if len(List) == 5:
        print('Your list contains', List)

for j in List:
    Sum = List[j] + Sum

print('The sum of your list is ', Sum)
print('The average of your list is', Sum / len(List))
