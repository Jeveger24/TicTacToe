import random


def drawBoard(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("~~~~~")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("~~~~~")
    print(board[1] + "|" + board[2] + "|" + board[3])


def choosingLetter():
    playerLetter = ""
    while not (playerLetter == "X" or playerLetter == "O"):
        playerLetter = input("Do you want the letter X or O? ").upper()
    if playerLetter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return "Computer"
    else:
        return "Player"


def playAgain():
    again = input("Do you want to play again? (Yes, No) ")
    return again.upper().startswith("Y")


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # across the top
            # across the middle
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            # across the bottom
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            # down the left side
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            # down the middle
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            # down the right side
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            # diagonal
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))  # diagonal


def getBoardCopy(board):
    dupiBoard = []
    for i in board:
        dupiBoard.append(i)
    return dupiBoard


def isSpaceFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):
    move = " "
    while (move not in "1 2 3 4 5 6 7 8 9".split()) or (not isSpaceFree(board, move)):
        move = input("Make your move! ")
        return int(move)


def randomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # check if computer can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # check if player can win in the next move and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # try to take the corners if free
    move = randomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # try to take the middle if free
    if isSpaceFree(board, 5):
        return 5

    # move on one of the sides
    return randomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("Welcome to Tic Tac Toe!")
while True:
    theBoard = [" "] * 10
    playerLetter, computerLetter = choosingLetter()
    turn = whoGoesFirst()
    print(turn, "will go first!")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "Player":
            # player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "Computer"
        else:
             # computer’s turn.
             move = getComputerMove(theBoard, computerLetter)
             makeMove(theBoard, computerLetter, move)

             if isWinner(theBoard, computerLetter):
                 drawBoard(theBoard)
                 print("The computer has beaten you! You lose.")
                 gameIsPlaying = False
             else:
                 if isBoardFull(theBoard):
                     drawBoard(theBoard)
                     print("The game is a tie!")
                     break
                 else:
                     turn = "Player"

    if not playAgain():
        break