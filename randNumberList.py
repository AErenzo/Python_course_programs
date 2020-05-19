import random

def randNumberList(a):
    l = []

    for i in range(a):
        number = random.randint(1, 6)
        l.append(number)

    return l

o = int(input('Please set the size of the list: '))

print(randNumberList(o))
