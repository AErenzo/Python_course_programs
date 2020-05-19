def temperature():
    temp = int(input('What is the temperature? '))

    if temp > 35:
        print(temp, '- Hot Day')
    elif temp >= 25 and temp <= 35:
        print(temp, '- Pleasant Day')
    elif temp >= 15:
        print(temp, '- Fairly Cool Day')
    else:
        print(temp, '- Best Wrap Up!')     
temperature()

        
