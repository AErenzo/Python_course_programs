import random 

def count(a, b):

    c = 0

    d = 'Number not found'
    
    while True:
        for i in range(len(a)):
            if numbers[i] == b:
                c += 1
        if c > 0:
            return c
        else:
            return d
            
        



numbers = []
while True:
    
    for i in range(15):
        number = random.randint(1, 10)
        numbers.append(number)
          
    if len(numbers) <= 1:
        continue
    else:
        C = int(input('Choose a number between 1 - 10 to see how many times its been chosen:  '))
        break
    

x = count(numbers, C)

print(x)

    
