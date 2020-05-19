while True:
    
    w = int(input('Please enter the width of your rectangle: '))
    h = int(input('Please enter the height of your rectangle: '))
    
    if w > 0 and w < 101:


        if h > 0 and h < 101:
            print('Area of recetangle is', w * h)
            print('Perimeter of rectangle is', (w + h) * 2)
            print()
            print('* ' * w)
            print('* \n' * h)
            print('* ' * w)
            break
        
        else:
            print('Please enter a value thats greater than 1 and less than or equal too 100.')
            continue
            
    else:
        print('Please enter a value thats greater than 1 and less than or equal too 100.')
        continue

        
