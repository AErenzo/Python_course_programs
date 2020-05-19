import random
List = []

for i in range(10):
    List.append(random.randint(1, 100))

maxi = List[0]

for j in range(1, 10):
    if List[j] > maxi:
        maxi = List[j]
        
print(List)        
print('The maxiumum value within your list is: ', maxi)
