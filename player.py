import random
import math

class Player():
    '''Class defining a generic player

    Methods
    -------

    getMove()
    '''

    def __init__(self,letter):
        self.letter = letter
    
    def getMove(self,game):
        '''Get the move from the player

        Parameters
        ----------

        Game : game
            The game being played
        '''
        pass

class Human(Player):
    '''Class defining a human player

    Methods
    -------

    getMove()
    '''

    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        '''Get the move from the player

        Parameters
        ----------

        Game : game
            The game being played
        
        Returns
        -------
        int : value
            The index of the move played
        '''
        valid_move = False
        value = None 
        # We loop while the move made by the player is invalid
        while not valid_move:
            move = input(self.letter + '\'s turn. Choose your next move (0-8) : ')
            try:
                # We cast the move to int to check a number has been given
                value = int(move)
                if value not in game.available_spots():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalide spot, try again')
        return value

class Computer(Player):
    '''Class defining a computer player

    Methods
    -------

    getMove()
    '''

    def __init__(self,letter):
        super().__init__(letter)
    
    def getMove(self,game):
        '''Get the move from the player

        Parameters
        ----------

        Game : game
            The game being played
        
        Returns
        -------

        int : move
            The spot chosen 
        '''
        move = random.choice(game.available_spots())
        return move

class GoodComputer(Player):
    '''Class defining a computer player

    Methods
    -------

    getMove()
    minimax()
    '''

    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        '''Get the move from the player

        Parameters
        ----------

        Game : game
            The game being played
        
        Returns
        -------

        int : move
            The spot chosen 
        '''
        if len(game.available_spots()) == 9:
            spot = random.choice(game.available_spots())
        else:
            spot = self.minimax(game, self.letter)['position']
        return spot
    
    def minimax(self, game_state, player):
        '''Get the move from the player

        Parameters
        ----------

        Game : game_state
            The status of the game
        
        str : player
            The player (letter)
        
        Returns
        -------

        dict : best
            Dictionnary containing the index and value of the best spot to play 
        '''
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        
        # We set the score of the previous move
        if game_state.current_winner == other_player:
            return  {'position': None, 
                     'score': 1*(game_state.number_empty_spots() +1) if other_player == max_player else -1 * (game_state.number_empty_spots() + 1)}
        
        # If the board is full, we set the score to 0
        elif not game_state.empty_spots():
            return {'position': None, 'score': 0}
        
        # We initialize the score
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        
        for possible_spot in game_state.available_spots():
            # We make a move
            game_state.make_move(possible_spot, player)
            # We execute the recursive function with new board and other player
            sim_score = self.minimax(game_state, other_player)

            # We reverse the move
            game_state.board[possible_spot] = ' '
            game_state.current_winner = None
            sim_score['position'] = possible_spot

            # We update the dictionnary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best



