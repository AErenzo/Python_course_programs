for i in range(1, 7):
    # below determines the spaces for each new line, to create the reverse pyramid affect
    print(" " * (7 - (8 - i)))
    for j in range(1, 8 - i):
        print(j, end = " ")
    
