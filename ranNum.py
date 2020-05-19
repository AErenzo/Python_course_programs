import random

def ranNum():
    
    N = random.randint(1, 10)

    guess = 0

    tries = 0

    print('Im thinking of a number \nbetween 1 and 10.')

    while guess != N and tries < 5:

        guess = int(input('What do you think it might be? '))

        if guess  < N:
            print('Your guess is too low')
        elif guess > N:
            print('Your guess is to high')
        else:
            break

        tries += 1

    if guess ==  N:
        print('You guessed it, well done! It took you', tries, 'tries to guess the correct number')
    else:
        print('Sorry you lost, you didnt guess the number within 5 tries.')

    retry = input('Would you like to play again? (y/n) ')
    
    if retry == 'y' or retry == 'Y':
        ranNum()
    else:
        exit

ranNum()
    
    
      
