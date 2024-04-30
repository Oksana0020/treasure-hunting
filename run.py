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

    @staticmethod
    def display_rules():
        """Display the short rules of the game."""
        print("""
        Welcome, Player!
    
        Rules:
        1. The objective of the game is to find three treasures hidden on a 10x10 grid while avoiding obstacles.
        2. Treasures are represented by 💰, bombs by 💣, water by 💧, and snakes by 🐍.
        3. You'll take turns guessing spots on the map to reveal what's hidden there.
        4. If you find a treasure, you earn a point. If you hit a bomb, the game ends.
        5. Water and snakes are harmless but may affect your strategy.
        6. The game ends when you find three treasures or hit three bombs.
    
        Let's begin!
        """)
    

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
        self.treasures = self.place_unique_items(25, "💰")
        for treasure in self.treasures:
            self.board[treasure] = "💰"

    def place_bombs(self):
        """Function to place bombs on the board"""
        self.bombs = self.place_unique_items(25, "💣")
        for bomb in self.bombs:
            self.board[bomb] = "💣"

    def place_water(self):
        """Function to place water on the board"""
        self.water = self.place_unique_items(25, "💧")
        for water in self.water:
            self.board[water] = "💧"

    def place_snakes(self):
        """Function to place snakes on the board"""
        self.snakes = self.place_unique_items(25, "🐍")
        for snake in self.snakes:
            self.board[snake] = "🐍"

    def place_unique_items(self, count, symbol):
        """Helper function to place unique items on the board"""
        items_placed = 0
        items = set()
        while items_placed < count:
            item = random.randint(0, 99)
            if self.board[item] == "□":
                items.add(item)
                items_placed += 1
                self.board[item] = symbol
        return list(items)

    def play(self):
        """Play function to create the play loop of the game.
        It iterates continuously while the game is on.
        Picture of treasure is taken from https://trinket.io/python/e2f2419064"""
        while self.game_on:
            print("Your turn, Player:")
            self.display_masked_board()
            self.user_turn()
            if self.user_hits == 3:
                print("Congratulations! You found 3 treasures and won the game!")
                print("This is how the board looked like in this game")
                self.display_board()
                print("That's your treasure, don't forget to take it!")
                print('''
 *******************************************************************************
           |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
 |                   |  ,-"_,=""     `"=.|                  |
 |___________________|__"=._o`"-._        `"=.______________|___________________
           |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
 |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
 |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
 |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
 |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
 ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
 /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
 ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
 /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
 ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
 /______/______/______/______/______/______/______/______/______/______/_____ /
 *******************************************************************************
 ''')
                self.game_on = False
                break
            self.display_masked_board()
            self.hunter_turn()
            if self.hunter_hits == 3:
                print("Hunter found 3 treasures and won the game!")
                print("This is how the board looked like in this game")
                self.display_board()
                self.game_on = False
                break

    def user_turn(self):
        """Function for the user's turn from input"""
        while True:
            user_guess = input("Your turn! Guess a spot by typing two symbols: first letter and second number between 1 and 10 (e.g. A1): ").upper()
            if self.validate_guess(user_guess):
                guess_index = self.map_guess_to_board_cell(user_guess)
                if self.masked_board[guess_index] != "□":
                    print("This spot is already open. Try one more time!")
                else:
                    self.hit(user_guess, "user")
                    break
            else:
                print("Invalid input! Please enter a letter between A-J and a number between 1-10.")

    def validate_guess(self, guess):
        """Validate the format of the user's guess"""
        if len(guess) < 2 or len(guess) > 3:
            return False
    
        column = guess[0]
        row = guess[1:]

        if column < 'A' or column > 'J':
            return False

        if not row.isdigit():
            return False

        row_num = int(row)
        if row_num < 1 or row_num > 10:
            return False

        return True


    def hunter_turn(self):
        """Function for the hunter's turn to generate and display hunter's turn"""
        hunter_guess = self.generate_hunter_guess()
        print("Hunter's turn:")
        print(f"Hunter guessed: {hunter_guess}")
        guess_index = self.map_guess_to_board_cell(hunter_guess)
        self.hit(guess_index, "hunter")
        self.display_masked_board()  

    def generate_hunter_guess(self):
        """Generate Hunter guessing using random"""
        while True:
            row = random.randint(1, 10)
            column = random.randint(0, 9)
            guess = chr(ord('A') + column) + str(row)
            guess_index = self.map_guess_to_board_cell(guess)
            if guess_index not in [self.user_hits] + [self.hunter_hits]:
                return guess

    def hit(self, guess, player):
        """Function for a hit on the board and Update if treasure found"""
        if player == "user":
            guess_index = self.map_guess_to_board_cell(guess)
        else:
            guess_index = guess  

        hit_result = self.evaluate_hit(guess_index)
        if player == "user":
            self.user_hits += hit_result
        else:
            self.hunter_hits += hit_result

        self.update_masked_board(guess_index)

    def update_masked_board(self, index):
        """Update masked board according to hit"""
        if index in self.water:
            self.masked_board[index] = "💧"  
        elif index in self.bombs:
            self.masked_board[index] = "💣"  
        elif index in self.snakes:
            self.masked_board[index] = "🐍"  
        elif index in self.treasures:
            self.masked_board[index] = "💰"
        else:
            self.masked_board[index] = "❌"

    def evaluate_hit(self, index):
        """Function to evaluate hit"""
        if index in self.water:
            print("You need to cross the river")
            return 0
        elif index in self.treasures:
            print("Wow! You found a treasure!")
            return 1
        elif index in self.bombs:
            print("Oops! You hit a bomb!")
            return 0
        elif index in self.snakes:
            print("Be aware! There are snakes. But you are lucky they are sleeping right now.")
            return 0
        else:
            print("Mmm... I smell treasure is somewhere near you")   
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

if __name__ == "__main__":
    TreasureHunt.display_rules()
    while True:
        game = TreasureHunt()
        game.initialize_board()
        game.place_items()
        game.play()
        choice = input("Would you like to play again? (1 for yes, 2 for no): ")
        if choice != "1":
            print("Goodbye! Have a nice day!")
            break

