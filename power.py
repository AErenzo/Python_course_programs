def power(x, n):
    r = x** n
    return r

print('Power function, enter a number and what you want to power it by')
print()

num = int(input('Please enter number: '))

P = int(input('Please enter power: '))

print(power(num, P))



