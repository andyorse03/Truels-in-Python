import random




#Creating the class for the player

class Player:

    def __init__(self, marksmanship: float, shooting_turn, strategy: str):
        self.marksmanship = marksmanship
        self.shooting_turn = shooting_turn
        self.strategy = strategy
    
    def shooting(self):
        if random.random <= self.marksmanship:
            return 1
        else:
            return 0
        
    




#Defining 3 players to be recalled in the following functions:

player_1 = Player(0.2, 1, 'c', 'b')
player_2 = Player(0.5, 2, 'c', 'a')
player_3 = Player(0.8, 3, 'b', 'c')

#Function for the basic truel (no absention, no suicide)

def truel_baseline(a: Player, b: Player, c: Player):
    pass
    
    




