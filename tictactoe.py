# CMPT 120 Intro to Programming
# Author: Your Name Here
# Created: YYYY-MM-DD
symbol = [ " ", "x", "o" ]
def printRow(row):
    # initialize output to the left border
    # for each square in the row...
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
    pass
def printBoard(board):
    print(' +-----------+')
    for row in range(3):
        for place in range(3):
            print(' | ' , end='')
            if board[row][place] == 0:
                board[row][place] = symbol[0]
            elif board[row][place] == 1:
                board[row][place] = symbol[1]
            elif board[row][place] == 2:
                board[row][place] = symbol[2]
            print(board[row][place], end='')
        print(' |')
        print(' +-----------+')
def markBoard(board, row, col, player):
        if board[row][col] == symbol[0]:
            board[row][col] = player
            return True
        else:
            print('That Spot is already taken.')
            print('Try again.\n')
            return False
def inputMove():
    try:
        a = int(input("What row? "))
        b = int(input("What Column? "))
    except:
        return 4,4
    return a,b
    
def getPlayerMove():
    row,col=inputMove()
    while row > 3 or col > 3:
        print('Must input 1 - 3\n')
        row,col=inputMove()
    return (row - 1,col - 1)
def hasBlanks(board):
    test = 0
    for row in range(3):
        for square in range(3):
            if board[row][square] == symbol[1] or\
               board[row][square] == symbol[2]:
                test = test + 1
                if test == 9:
                    print('Game over.')
                    return False
    return True
def main():
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    player = 1
    printBoard(board)
    while hasBlanks(board):
        x = False
        while x is False:
            row,col = getPlayerMove()
            x = markBoard(board,row,col,player)
        player = player % 2 + 1
        printBoard(board)
main()
