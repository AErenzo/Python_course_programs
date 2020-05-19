def front_times(a, b):
    c = a[0:b]
    return c


string = input('Please enter a string value, could be an object or name: ')

print()

print('I will shorten the value you just entered.')

front = int(input('Please enter the length at which you wish for me to shorten your string: '))

N = int(input('How may copies do you want: '))

r = front_times(string, front) * 3

r.join('')

print(r)


    
