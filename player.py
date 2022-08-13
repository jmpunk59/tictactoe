import random
import math

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

class GoodComputer(Player):

    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        if len(game.available_spots()) == 9:
            spot = random.choice(game.available_spots())
        else:
            spot = self.minimax(game, self.letter)['position']
        return spot
    
    def minimax(self, game_state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        #first, we want to check if the previous move is a winner
        #this is our base case
        if game_state.current_winner == other_player:
            return  {'position': None, 
                     'score': 1*(game_state.number_empty_spots() +1) if other_player == max_player else -1 * (game_state.number_empty_spots() + 1)}
        
        elif not game_state.empty_spots():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_spot in game_state.available_spots():
            game_state.make_move(possible_spot, player)

            sim_score = self.minimax(game_state, other_player)

            game_state.board[possible_spot] = ' '
            game_state.current_winner = None
            sim_score['position'] = possible_spot

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best



