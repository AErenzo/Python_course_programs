def maxFunction(a, b):
    if a < b:
        return b
    else:
        return a

print('Input your number and ill tell you which is higher! MAX')

a = int(input('Please enter a number (a): '))
b = int(input('Please enter a number (b): '))

x = maxFunction(a, b)
print('Maximum value is', x)
