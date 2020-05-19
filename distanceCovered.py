def distanceCovered():
    print('Hello, i will help work how much distance you have covered.')
    print()
    
    time = int(input('Please tell me how long you were travelling for per hour? '))
    print()
    speed = int(input('Please tell me the speed at which you was travelling? '))
    print()

    distance = time * speed

    print('In ', time, 'hours, you managed to travel the distance of ', distance, 'miles')

distanceCovered()
