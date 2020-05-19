myList = ['Bob', 'Sally', 'Ian', 'Burt', 'Digby']

loc = -1

user_key = input('Please enter the value you wish to search for: ')

for i in range(len(myList)):
    if user_key == myList[i]:
        loc = i
       # print(user_key, 'found at index', i)
        break
   # else:
     #   print('Sorry user not found')

if loc == -1:
    print('Sorry user not found')
else:
    print(user_key, 'found at index', i)
