class TreasureHunt:
    def __init__(self):
        """
        Represents the game board and masked board available when game is on
        """
        self.board = [" " for _ in range(100)]
        self.masked_board = ["□" for _ in range(100)]  
        self.game_on = True

    def initialize_board(self):
        """Initialize the game board."""
        for i in range(100):
            self.board[i] = "□"

    def display_masked_board(self):
        """Display the masked board with row numbers and column letters."""
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


game = TreasureHunt()
game.initialize_board()
print("First Game Board:")
game.display_board()

