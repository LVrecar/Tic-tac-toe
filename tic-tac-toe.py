
import algorithm
from tkinter import *

def change(x):
    if not gameOver.get():
        if x.get() == "":
            x.set(turn.get())
            turn.set("O") if turn.get() == "X" else turn.set("X")
        board = updateBoard(rows)
        winner = checkForVictory()
        if winner != "":
            endGame(winner)
        else:
            nextTurn()
    else:
        print("Game over!")

def updateBoard(rows):
    board = []
    for i in rows:
        row = []
        for j in i:
            row.append(j.get())
        board.append(row)
    return board

def checkForVictory():
    board = updateBoard(rows)
    options = algorithm.makeOptions(board)

    for option in options:
        value = option[0]
        if value == option[1] == option[2] and value != "":
            gameOver.set(True)
            return value

    full = 0
    for i in board:
        for j in i:
            if j != "":
                full += 1
    if full == 9:
        gameOver.set(True)
        return "draw"

    return ""
  
def nextTurn():
    board = updateBoard(rows)
    if turn.get() == computerSymbol.get():
        pos = algorithm.analyse(board, computerSymbol.get())
        buttonBoard[pos[0]][pos[1]].invoke()

def endGame(winner):
    if winner == "draw":
        draws.set(draws.get()+1)
    elif winner == computerSymbol.get():
        computerScore.set(computerScore.get()+1)
    else:
        playerScore.set(playerScore.get()+1)

def reset():
    if gameOver.get():
        for row in rows:
            for i in row:
                i.set("")
        turn.set("X")
        updateBoard(rows)
        gameOver.set(False)
        computerSymbol.set("O") if computerSymbol.get() == "X" else computerSymbol.set("X")
        nextTurn()

root = Tk()
root.title("Tic-Tac-AI")

f00 = StringVar(root)
f01 = StringVar(root)
f02 = StringVar(root)
f10 = StringVar(root)
f11 = StringVar(root)
f12 = StringVar(root)
f20 = StringVar(root)
f21 = StringVar(root)
f22 = StringVar(root)

rows = [[f00, f01, f02],
        [f10, f11, f12],
        [f20, f21, f22]]

board = updateBoard(rows)
gameOver = BooleanVar(root)
gameOver.set(False)
computerSymbol = StringVar(root)
computerSymbol.set("X")

turn = StringVar(root)
turn.set("X")

b00 = Button(root, textvariable = f00, command = lambda: change(f00), width = 3, font = ("serif", 32, "bold"))
b00.grid(row=0, column=0)
b01 = Button(root, textvariable = f01, command = lambda: change(f01), width = 3, font = ("serif", 32, "bold"))
b01.grid(row=0, column=1)
b02 = Button(root, textvariable = f02, command = lambda: change(f02), width = 3, font = ("serif", 32, "bold"))
b02.grid(row=0, column=2)
b10 = Button(root, textvariable = f10, command = lambda: change(f10), width = 3, font = ("serif", 32, "bold"))
b10.grid(row=1, column=0)
b11 = Button(root, textvariable = f11, command = lambda: change(f11), width = 3, font = ("serif", 32, "bold"))
b11.grid(row=1, column=1)
b12 = Button(root, textvariable = f12, command = lambda: change(f12), width = 3, font = ("serif", 32, "bold"))
b12.grid(row=1, column=2)
b20 = Button(root, textvariable = f20, command = lambda: change(f20), width = 3, font = ("serif", 32, "bold"))
b20.grid(row=2, column=0)
b21 = Button(root, textvariable = f21, command = lambda: change(f21), width = 3, font = ("serif", 32, "bold"))
b21.grid(row=2, column=1)
b22 = Button(root, textvariable = f22, command = lambda: change(f22), width = 3, font = ("serif", 32, "bold"))
b22.grid(row=2, column=2)

buttonBoard = [[b00, b01, b02],
               [b10, b11, b12],
               [b20, b21, b22]]

playerScore = IntVar(root)
computerScore = IntVar(root)
draws = IntVar(root)

Label(root, text = "Player:").grid(row = 0, column = 5)
Label(root, textvariable = playerScore).grid(row = 0, column = 6)
Label(root, text = "Draws:").grid(row = 0, column = 7)
Label(root, textvariable = draws).grid(row = 0, column = 8)
Label(root, text = "Computer:").grid(row = 0, column = 9)
Label(root, textvariable = computerScore).grid(row = 0, column = 10)
Label(root, text = "Turn: ").grid(row = 1, column = 5)
Label(root, textvariable = turn, width = 3, justify = LEFT).grid(row = 1, column = 6)
Button(root, text = "PLAY AGAIN", command = lambda: reset()).grid(row=2, column = 9)
Button(root, text  = "QUIT", command = lambda: quit()).grid(row = 2, column = 10)

nextTurn()
root.mainloop()