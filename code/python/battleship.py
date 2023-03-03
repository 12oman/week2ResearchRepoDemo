import random

# Define constants
EMPTY = 0
SHIP = 1
MISS = 2
HIT = 3

# Define function to create an empty game board
def create_board():
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(EMPTY)
        board.append(row)
    return board

# Define function to print the game board
def print_board(board):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(10):
        row = chr(i + 65)
        for j in range(10):
            if board[i][j] == EMPTY:
                row += "  "
            elif board[i][j] == SHIP:
                row += "  "
            elif board[i][j] == MISS:
                row += " O"
            elif board[i][j] == HIT:
                row += " X"
        print(row)

# Define function to place a ship on the board
def place_ship(board, ship):
    for x, y in ship:
        board[x][y] = SHIP

# Define function to generate a random ship
def generate_ship():
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    direction = random.randint(0, 1)
    ship = []
    for i in range(5):
        if direction == 0:
            ship.append((x+i, y))
        else:
            ship.append((x, y+i))
    return ship

# Define function to get user input for firing
def get_fire_coords():
    while True:
        try:
            coords = input("Enter coordinates to fire at (e.g. A1, B2, etc.): ")
            x, y = ord(coords[0].upper()) - 65, int(coords[1:]) - 1
            if 0 <= x < 10 and 0 <= y < 10:
                return x, y
            else:
                print("Invalid coordinates! Please enter a valid coordinate (e.g. A1, B2, etc.)")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid coordinate (e.g. A1, B2, etc.)")

# Define function to run the game
def play_battleship():
    board = create_board()
    ships = []
    for i in range(5):
        while True:
            ship = generate_ship()
            overlap = False
            for x, y in ship:
                if board[x][y] == SHIP:
                    overlap = True
                    break
            if not overlap:
                place_ship(board, ship)
                ships.append(ship)
                break
    print("Let's play Battleship!")
    while True:
        print_board(board)
        x, y = get_fire_coords()
        if board[x][y] == EMPTY:
            board[x][y] = MISS
            print("Miss!")
        elif board[x][y] == SHIP:
            board[x][y] = HIT
            print("Hit!")
            for ship in ships:
                if (x, y) in ship:
                    ship.remove((x, y))
                    if len(ship) == 0:
                        print_board(board)
                        print("You sunk my battleship!")
                        return
        else:
            print("You already fired at that location!")

play_battleship()