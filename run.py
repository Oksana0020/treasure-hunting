import random

class TreasureHunt:
    """
    Creates an instance of TreasureHunt
    """
    def __init__(self):
        self.board = [" " for _ in range(100)]
        self.masked_board = ["□" for _ in range(100)]  
        self.treasures = []
        self.bombs = []
        self.water = []
        self.snakes = []
        self.user_hits = 0
        self.hunter_hits = 0
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
        """Function to place bombs on the board"""
        self.bombs = random.sample(range(100), 10)
        for bomb in self.bombs:
            self.board[bomb] = "💣"
    
    def place_water(self):
        """Function to place water on the board"""
        self.water = random.sample(range(100), 15)
        for water in self.water:
            self.board[water] = "💧"

    def place_snakes(self):
        """Function to place snakes on the board"""
        self.snakes = random.sample(range(100), 25)
        for snake in self.snakes:
            self.board[snake] = "🐍"

    def play(self):
        """Play function to create the play loop of the game.
        It iterates continuously while the game is on"""
        while self.game_on:
            print("Your turn, Player:")
            self.display_masked_board()
            self.user_turn()
            if self.user_hits == 3:
                self.display_board()
                print("Congratulations! You found 3 treasures and won the game!")
                self.game_on = False
                break
            self.display_masked_board()
            self.hunter_turn()
            if self.hunter_hits == 3:
                self.display_board()
                print("Hunter found 3 treasures and won the game!")
                self.game_on = False
                break

    def user_turn(self):
        """Function for the user's turn from input"""
        user_guess = input("Your turn! Guess a spot by typing two symbols: first letter and second number between1 and 10 (e.g. A1): ").upper()
        self.hit(user_guess, "user")

    def hunter_turn(self):
        """Function for the hunter's turn to generate and display hunter's turn"""
        hunter_guess = self.generate_hunter_guess()
        print("Hunter's turn:")
        print(f"Hunter guessed: {hunter_guess}")
        self.hit(hunter_guess, "hunter")
        self.display_masked_board()
    
    def generate_hunter_guess(self):
        """Generate Hunter guessing using random"""
        while True:
            guess = random.randint(0, 99)
            if guess not in self.treasures + self.bombs + self.water + self.snakes:
                return self.map_index_to_board_cell(guess)

    def hit(self, guess, player):
        """Function for a hit on the board and
        Update if treasure found"""
        guess_index = self.map_guess_to_board_cell(guess)
        hit_result = self.evaluate_hit(guess_index)
        if player == "user":
            self.user_hits += hit_result
            if hit_result == 1:
                self.masked_board[guess_index] = "💰"  
            else:
                self.update_masked_board(guess_index)
        else:
            self.hunter_hits += hit_result
            if hit_result == 1:
                self.masked_board[guess_index] = "💰"  
            else:
                self.update_masked_board(guess_index)

    def evaluate_hit(self, index):
        """Function to evaluate hit"""
        if index in self.treasures:
            print("Wow! You found a treasure!")
            return 1
        elif index in self.bombs:
            print("Oops!You hit a bomb!")
            self.game_on = False
            return 0
        elif index in self.water:
            print("You need to cross the river")
            return 0
        elif index in self.snakes:
            print("Be aware! There are snakes. But you are lucky they are sleeping right now.")
            return 0
        else:
            print("Mmm... I smell treasure is somewhere near you.")
            return 0  

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
game.place_items()
game.play()

