from player import Human, Computer, GoodComputer

class Game():
    '''Class representing the TicTacToe game

        Methods
        -------

        print_board(self)
        print_board_nums(self)
        available_spots(self)
        empty_spots(self)
        number_empty_spots(self)
        make_move(self,spot,letter)
        winner(self,spot,letter)
    '''

    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None
    
    def print_board(self):
        '''Prints the current TicTacToe board
        '''

        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def print_board_nums(self):
        '''Prints the board with the indices
        '''

        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_spots(self):
        '''Returns the spots the player can choose
        '''

        # For each index,value , add index if spot is available
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_spots(self):
        '''Determine wether there is a spot left or not
        '''

        return ' ' in self.board
    
    def number_empty_spots(self):
        '''Return the number of empty spot
        '''

        return self.board.count(' ')
    
    def make_move(self, spot, letter):
        '''Execute the next move

        Parameters
        ----------

        int: spot
            The spot to be played
        char: letter
            The player
        
        Returns
        -------

        True : If the move was made on a empty spot 
        False: If the move is not a valid move
        '''

        if self.board[spot] == ' ':
            self.board[spot] = letter
            if self.winner(spot,letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, spot, letter):
        '''Checks if the move was a winning move
        '''

        # We check the rows
        row_ind = spot // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([square == letter for square in row]):
            return True
        
        # We check the columns
        col_ind = spot % 3
        col = [self.board[col_ind + i*3] for i in range(3)]
        if all([square == letter for square in col]):
            return True
        
        # We check the diagonals
        if spot % 2 == 0:
            right_diag = [self.board[i] for i in [0,4,8]]
            if all([square == letter for square in right_diag]):
                return True
            left_diag = [self.board[i] for i in [2,4,6]]
            if all([square == letter for square in left_diag]):
                return True
        
        return False

    

def play(game, x_player, o_player, verbose=True):
    ''' Plays the TicTacToe game

    Parameters
    ----------

    Game : game
        The TicTacToe game representation
    Player : x_player
        The player that plays X
    Player : o_player
        The payer that plays O
    Bool : verbose
        Allows to enable the verbose mode (default = True)
    '''
    if verbose:
        game.print_board_nums()
    
    letter = 'X'
    while game.empty_spots():
        if letter == 'O':
            move = o_player.getMove(game)
        else:
            move = x_player.getMove(game)
        
        if game.make_move(move, letter):
            if verbose:
                print(letter + f' makes a move to spot {move}')
                game.print_board()

        if game.current_winner != None:
            if verbose:
                print(letter + ' wins')
            return letter

        letter = 'O' if letter == 'X' else 'X'
    
    if verbose:
        print('It\'s a tie.')    


if __name__ == "__main__":
    x = input("Choose the x_player (H for Human, C for Computer, G for GoodComputer : ").upper()
    while (x != 'H' and x != 'C' and x != 'G'):
        x = input("Wrong input, choose the x_player (H for Human, C for Computer, G for GoodComputer : ").upper()
    x_player = Human('X') if x == 'H' else (Computer('X') if x == 'C' else GoodComputer('X'))
    
    o = input("Choose the o_player (H for Human, C for Computer, G for GoodComputer : ").upper()
    while (o != 'H' and o != 'C' and o != 'G'):
        o = input("Wrong input, choose the x_player (H for Human, C for Computer, G for GoodComputer : ").upper()
    o_player = Human('O') if o == 'H' else (Computer('O') if o == 'C' else GoodComputer('O'))

    game = Game()
    play(game, x_player, o_player)

