board = [".", ".", ".",
         ".", ".", ".",
         ".", ".", ".", ]

CurrentPlyer1 = "X"
CurrentPlyer2 = "0"
winner = None

def printboard():
    print(board(".") + " | " + board(".") + " | " + board("."))