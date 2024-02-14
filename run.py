import random

class TreasureHunt:
    def __init__(self):
        """
        Represents the game board and masked board available when game is on
        """
        self.board = [" " for _ in range(100)]
        self.masked_board = ["□" for _ in range(100)]  
        self.treasures = []
        self.bombs = []
        self.water = []
        self.snakes = []
        self.game_on = True

    def initialize_board(self):
        """Initialize the game board."""
        for i in range(100):
            self.board[i] = "□"

    def place_items(self):
        """Place all items on the board"""
        self.place_treasure()
        self.place_bombs()
        self.place_water()
        self.place_snakes()

    def place_treasure(self):
        """Function to place treasures on the board"""
        self.treasures = random.sample(range(100), 20)
        for treasure in self.treasures:
            self.board[treasure] = "💰"

    def place_bombs(self):
        """# Function to place bombs on the board""""
        self.bombs = random.sample(range(100), 10)
        for bomb in self.bombs:
            self.board[bomb] = "💣"


    def display_masked_board(self):
        """Display masked board with row numbers and column letters."""
        print("    " + "  ".join([chr(65 + i) for i in range(10)]))
        for i in range(10):
            line = f"{i + 1:2d}  "
            line += "  ".join([self.masked_board[i * 10 + j] for j in range(10)])
            print(line)

    def display_board(self):
        """Display the game board with row numbers and column letters."""
        print("    " + "  ".join([chr(65 + i) for i in range(10)]))
        for i in range(10):
            line = f"{i + 1:2d}  "
            line += "  ".join([self.board[i * 10 + j] for j in range(10)])
            print(line)
    
    def map_guess_to_board_cell(self, guess):
        """maps user guess to the corresponding index on the game board:
        calculates the column index by subtracting the ASCII value of 'A' from the ASCII value of the first character 
        of the guess,and row index by subtracting 1 from the integer value of the remaining characters of the guess"""
        column = ord(guess[0]) - ord('A')
        row = int(guess[1:]) - 1
        return row * 10 + column

    def map_index_to_board_cell(self, index):
        """maps a board index to the corresponding cell on the game board
        calculates row by dividing the index by 10 (because there are 10 cells per row) 
        and column by taking the remainder of the index divided by 10,
        then converts the row and column to their corresponding characters using ASCII and returns 
        # board cell coordinates"""
        row = index // 10
        column = index % 10
        return chr(ord('A') + column) + str(row + 1)



game = TreasureHunt()
game.initialize_board()
print("First Game Board:")
game.display_board()
game.display_masked_board()

