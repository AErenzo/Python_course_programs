List = [10, 58, 46, 5, 32, 20]

n = len(List)

print('Your list before sorting:', List)

for k in range(1, n): # for loop will run 9 iteration as we start from 1
    for j in range(n - k): # n - k will be 9 on the first iteration
        if List[j] > List[j + 1]: # if the List index[j] is greater than the next
            temp = List[j] # store the value of index[j] in a var called temp
            List[j] = List[j + 1] # overwrite the index[j] with the one next to it
            List[j + 1] = temp # then overwrite index[j+1] with the value stored in temp
print('Your sorted list is', List)
