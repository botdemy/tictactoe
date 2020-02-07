#-------------------------------------------------------------------------------
# Welcome to Tic-Tac-Toe Project
# In this project, we'll write a Python code that lets you play Tic-Tac-Toe
# against your friend or against CPU
#-------------------------------------------------------------------------------
# Insert your code below

# setup board
def drawboard():
    print("   a   b   c")
    print("")
    print("1 ",board[0]," ",board[1]," ",board[2])
    print("")
    print("2 ",board[3]," ",board[4]," ",board[5])
    print("")
    print("3 ",board[6]," ",board[7]," ",board[8])


def taketurn():

    validinput = False

    while not validinput:
        #you make a move
        print("Player " + whoseturn + ", make your move.")
        mymove = input()

        if mymove == "a1":
            cellnum = 0
        elif mymove == "b1":
            cellnum = 1
        elif mymove == "c1":
            cellnum = 2
        elif mymove == "a2":
            cellnum = 3
        elif mymove == "b2":
            cellnum = 4
        elif mymove == "c2":
            cellnum = 5
        elif mymove == "a3":
            cellnum = 6
        elif mymove == "b3":
            cellnum = 7
        elif mymove == "c3":
            cellnum = 8
        else:
            #print("Invalid move. Try again.")
            cellnum = None

        if cellnum == None:
            print("Invalid move. Try again.")
        elif board[cellnum] != '.':
            print("Too bad. It's taken.")
        else:
            board[cellnum] = whoseturn
            validinput = True


    #test
    #print(cellnum)

# main
board = ['.']*9
#board = ['.','.','.','.','.','.','.','.','.']

whoseturn = "X"
gameover = False


while not gameover:
    drawboard()
    taketurn()
    #TODO: define when we want to exit this loop?
    #1) when somebody wins
    #2) when all the spots are gone
    #else: alternate player and keep playing
    if whoseturn == "X":
        whoseturn = "O"
    else:
        whoseturn = "X"


#take turns

