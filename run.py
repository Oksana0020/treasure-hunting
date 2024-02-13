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

    def display_board(self):
        """Display the game board."""
        for i in range(0, len(self.board), 10):
            line = ' '.join([f'{cell:<2}' for cell in self.board[i:i + 10]])
            print(line)


game = TreasureHunt()
game.initialize_board()
print("First Game Board:")
game.display_board()

