import random

class Player():

    def __init__(self,letter):
        self.letter = letter
    
    def getMove(self,game):
        pass

class Human(Player):

    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        valid_move = False
        value = None 
        while not valid_move:
            move = input(self.letter + '\'s turn. Choose your next move (0-8) : ')
            try:
                value = int(move)
                if value not in game.available_spots():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalide spot, try again')
        return value

class Computer(Player):

    def __init__(self,letter):
        super().__init__(letter)
    
    def getMove(self,game):
        move = random.choice(game.available_spots())
        return move
    