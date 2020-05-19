def primeNumber():
    
    N = int(input('Select the range you would like to find the prime numbers of:  '))
    
    C = 0
    
    if N > 1:
        
        for i in range(2, N + 1):
            isPrime = True
            
            for j in range(2, i // 2 + 1):
                
                if i % j == 0:
                    isPrime = False
                    break

            if isPrime == True:
                print(i, 'is a prime number')
                print()
                C += 1
                
        print(C, 'Prime numbers found')
                   
    else:
        print('Please enter a number greater than ')
        again = input('Would you like another go? (y/n): ')
        if again == 'Y' or again == 'y':
            primeNumber()
        else:
            exit

        
primeNumber()


