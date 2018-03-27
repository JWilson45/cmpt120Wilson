# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
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
    # check to see whether the desired square is blank
        if board[row][col] == symbol[0]:
            board[row][col] = player
            return True
        else:
            print('That Spot is already taken.')
            print('Try again.\n')
            return False
    # if so, set it to the player number
def inputMove():
    a = int(input("What row?"))
    b = int(input("What Column?"))
    return a,b
    
def getPlayerMove():
    row,col=inputMove()
    while row > 3 or col > 3:
        print('Must input 1 - 3\n')
        row,col=inputMove()
    return (row - 1,col - 1)
def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    return True # if no square is blank, return False
def main():
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        x = False
        while x is False:
            row,col = getPlayerMove()
            x = markBoard(board,row,col,player)
        player = player % 2 + 1
main()
