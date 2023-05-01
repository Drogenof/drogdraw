import random

score = [[wins],[loses]]
player_count = 0

class DrogsDraw:
    def __init__(self):
        self.score = 0
        self.choice = None
        self.rules = {
             "earth": ["steel", "lightning", "fire"],
            "wind": ["earth", "Drog", "water"],
            "steel": ["wind", "lightning", "fire"],
            "lightning": ["wind", "Drog", "water"],
            "Drog": ["earth", "steel", "fire"],
            "fire": ["steel", "wind", "Drog"],
            "water": ["earth", "fire", "steel"]
        }

    def compare(self, choice1, choice2):
        if choice1 == choice2:
            return 0
        elif choice2 in self.rules[choice1]:
            return 1
        else:
            return -1

    def player_count(self, player_count, players):
        self.player_count = input("Would you like to face: 1)other opponents, or 2)practice with the computer")
        if player_count == 1:
            players == 2
        else:
            players == 1 
            return players

    def intro(self):
        self.intro = ""   

     def play(self):
        print("f{intro}")
        self.player1.choose()
        self.player2.random_choice()
        self.selection_player = self.player1.choose()
        self.selection_computer = self.player2.random_choice() 
        print(f"You have selected: {self.selection_player} And your opponent had selected: {self.selection_computer} ")
        result = self.compare(self.player1.choice, self.player2.choice)
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print(f"{self.player1.name} wins!")
            self.player1.score += 1
        else:
            print(f"{self.player2.name} wins!")
            self.player2.score += 1    

    def print_score(self):
        print(f"{self.player1.name}: {self.player1.score}")
        print(f"{self.player2.name}: {self.player2.score}")            

game = DrogsDraw()

while True:
    game.play()
    game.print_score()
    answer = input('Do you want to continue? (y/n):').lower()

    if answer.lower().startswith("y"):

      print("ok, carry on then")

    elif answer.lower().startswith("n"):

      print("ok, sayonnara")

      exit()        