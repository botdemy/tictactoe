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

# main
board = ['.']*9
drawboard()

whoseturn = "X"
gameover = False

while not gameover:
    taketurn(whoseturn)
    if whoseturn == "X":
        whoseturn = "O"
    else:
        whoseturn = "X"
#take turns

