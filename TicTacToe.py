import random 

# function that prints of the board
def printBoard():
    print('+---+---+---+')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('+---+---+---+')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('+---+---+---+')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('+---+---+---+')



# fucntion to determine winner
def isWinner(char):
    # horizontal winning combinations
    if board[0] == char and board[1] == char and board[2] == char:
        return True
    elif board[3] == char and board[4] == char and board[5] == char:
        return True
    elif board[6] == char and board[7] == char and board[8] == char:
        return True

    # vertical winning combinations
    elif board[0] == char and board[3] == char and board[6] == char:
        return True
    elif board[1] == char and board[4] == char and board[7] == char:
        return True
    elif board[2] == char and board[5] == char and board[8] == char:
        return True

    # diaganol winning combinations
    elif board[0] == char and board[4] == char and board[8] == char:
        return True
    elif board[2] == char and board[4] == char and board[6] == char:
        return True
    else:
        return False


# function to check if there is any blank spaces on the board - resulting in a tie
def isTie():
    if ' ' not in board:
        return True
    else:
        return False


# function to allow user to choose a side
def chooseSides():
    side = ''
    while not (side == 'X' or side == 'O'):
        side = input('Do you want to be X or O? ').upper()
    return side


# function determines which side goes first, using the randint
def Toss():
    if random.randint(0, 1) == 0:
        return 'X'
    else:
        return 'O'

# repeat condition flag
finished = False

# main loop - used to repeat the process if user wishes to play again
while not finished:
    
    # board variable - list of empty spaces
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']

    # condition - calling chooseSides function to determine which which side each player is 
    if chooseSides() == 'X':
        print('Your are X')
    else:
        print('Your are O')

    # empty player list 
    players = []

    # conditional - help determine order or players using the Toss function
    if Toss() == 'X':
        print('X wins the toss')
        players = ['X', 'O']
    else:
        players = ['O', 'X']
        print('O wins the toss')
        
    # call printBoard()
    printBoard()



    #Playing loop
    while True:
        
        # Player position loop
        while True:
            print(players[0], "'s turn -", end = ' ')
            p1 = int(input('Choose a position on the board (1-9): ')) - 1

            # if position chosen by p1 is blank - send the position to p1 side
            if board[p1] == ' ':
                board[p1] = players[0]
                break
            else:
                print('That poisition is already taken')
                continue

        # call printBoard()
        printBoard()

        # conditional - calling isWinner function, checking for a winner after X's turn
        if isWinner(players[0]):
            print(players[0], 'has won')
            break

        # conditional - calling isTie function, checking for a tie
        if isTie():
            print('Its a tie!')
            break
        
        # Player position loop
        while True:
            print(players[1], "'s turn -", end = ' ')
            p2 = int(input('Player # 2: Choose a position on the board (1-9)')) -1

            # if position chosen by p2 is blank - send the position to p2 side
            if board[p2] == ' ':
                board[p2] = players[1]
                break
            else:
                print('That poisition is already taken')
                continue

        printBoard()
        
        # conditional - calling isWinner function, checking for a winner after O's turn
        if isWinner(players[1]) == True:
            print(players[1], 'has won')
            break
        
        # conditional - calling isTie function, checking for a tie
        if isTie():
            print('Its a tie!')
            break

    r = input('Do you want to play again? (y/n) ').lower()

    if r == 'y':
        continue
    else:
        print('Thanks for playing!')
        finished = True

