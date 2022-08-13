from player import Human
from player import Computer

class Game():

    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_spots(self):
        # For each index,value , add index if spot is available
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_spots(self):
        return ' ' in self.board
    
    def number_empty_spots(self):
        return self.board.count(' ')
    
    def make_move(self, spot, letter):
        if self.board[spot] == ' ':
            self.board[spot] = letter
            if self.winner(spot,letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, spot, letter):
        row_ind = spot // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([square == letter for square in row]):
            return True
        
        col_ind = spot % 3
        col = [self.board[col_ind + i*3] for i in range(3)]
        if all([square == letter for square in col]):
            return True
        
        if spot % 2 == 0:
            right_diag = [self.board[i] for i in [0,4,8]]
            if all([square == letter for square in right_diag]):
                return True
            left_diag = [self.board[i] for i in [2,4,6]]
            if all([square == letter for square in left_diag]):
                return True
        
        return False

    

def play(game, x_player, o_player, verbose=True):
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
    x_player = Human('X')
    o_player = Computer('O')
    game = Game()
    play(game, x_player, o_player)

