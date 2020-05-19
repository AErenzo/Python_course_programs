dataList = [10, 20, 25, 46, 55, 65, 78, 82, 91, 100]

Location = -1

key = int(input('What page would you like to see? '))

# lBound
l = 0
# uBound
u = len(dataList) -1

# binearySearch
m = (l + u) // 2

while l <= u and dataList[m] != key:
    if key < dataList[m]:
         u = m - 1
    else:
         l = m + 1
    m = (l + u) // 2
    
if dataList[m] == key:
    location = m
    print('Value was found at ', location)
else:
    print('Value not found')
    
