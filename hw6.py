from enum import Enum

class Move:
    INVALID_COORDINATE = -1 #since 0 is a valid board coordinate in a 0-based indexing system
    
    def __init__(self, row, col, value=None):
        if value is None:
            self.row = self.INVALID_COORDINATE
            self.col = self.INVALID_COORDINATE
        else:
            self.row = row
            self.col = col
            self.value = value

class Player(Enum):
    X = 'X'
    O = 'O'

class GameState:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
    
    def game_over(self):
        # Check if game is won
        for i in range(3):
            # Check rows
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != None):
                return True
            # Check columns
            if (self.board[0][i] == self.board[1][i] == self.board[2][i] != None):
                return True
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != None):
            return True
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] != None):
            return True
        
        # Check if board is full
        for row in self.board:
            if None in row:
                return False
        return True

    def winner(self):
        # Check rows, columns and diagonals
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != None):
                return self.board[i][0]
            if (self.board[0][i] == self.board[1][i] == self.board[2][i] != None):
                return self.board[0][i]
        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != None):
            return self.board[0][0]
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] != None):
            return self.board[0][2]
        
        return None

    def __str__(self):
        result = ""
        for row in self.board:
            result += "|".join(str(cell) for cell in row) + "\n"
        return result.strip()

    def spot(self, row, col):
        piece = self.board[row][col]
        return piece if piece != None else None  

    def move(self, row, col, player):
        # Check if the spot is already occupied
        if self.board[row][col] != None:  
            return None
        
        new_state = GameState()
        # Copy the current board
        for i in range(3):
            for j in range(3):
                new_state.board[i][j] = self.board[i][j]
        # Place the new piece
        new_state.board[row][col] = player
        return new_state

class TicTacToeSolver:
    def find_best_move(self, state: GameState, player: Player):
        return self.solve_my_move(state, float('-inf'), float('inf'), player)
    
    def solve_my_move(self, state: GameState, alpha: float, beta: float, player: Player):
        if state.game_over():
            winner = state.winner()
            if winner == player:
                return Move(0, 0, 1)
            elif winner is None:
                return Move(0, 0, 0)
            else:
                return Move(0, 0, -1)
        
        best_move = None
        
        for row in range(3):
            for col in range(3):
                if state.board[row][col] is None:
                    # Get new state after move
                    new_state = state.move(row, col, player)
                    opponent = Player.O if player == Player.X else Player.X
                    
                    # Store solve_opponent_move result in child variable
                    child = self.solve_opponent_move(new_state, beta, alpha, opponent)
                    child_value = -child.value
                    
                    if best_move is None or child_value > best_move.value:
                        best_move = Move(row, col, child_value)
                    
                    alpha = max(alpha, best_move.value)
                    if alpha >= beta:
                        break
        
        return best_move

    def solve_opponent_move(self, state: GameState, alpha: float, beta: float, player: Player):
        # If game is over, return the OPPOSITE score compared to solve_my_move
        if state.game_over():
            winner = state.winner()
            if winner == player:
                return Move(0, 0, -1)  # Player wins (but negative since opponent's view)
            elif winner is None:
                return Move(0, 0, 0)  # Draw (same as before)
            else:
                return Move(0, 0, 1)  # Opponent wins 
        
        best_move = None
        
        for row in range(3):
            for col in range(3):
                if state.board[row][col] is None:
                    new_state = state.move(row, col, player)
                    opponent = Player.O if player == Player.X else Player.X

                    child = self.solve_my_move(new_state, beta, alpha, opponent)
                    child_value = -child.value  # Negate the value
                    
                    if best_move is None or child_value > best_move.value:
                        best_move = Move(row, col, child_value)
                    
                    beta = min(beta, best_move.value)

                    if beta <= alpha:
                        break
        
        return best_move

def main():
   
    game_state = GameState()
    solver = TicTacToeSolver()
    current_player = Player.X
    
  
    while not game_state.game_over():
        print(f"\nCurrent board:")
        print(game_state)
        print(f"\n{current_player.value}'s turn")
        
        # Find and make the best move
        best_move = solver.find_best_move(game_state, current_player)
        game_state = game_state.move(best_move.row, best_move.col, current_player)
        
        # Switch players
        current_player = Player.O if current_player == Player.X else Player.X
    
    
    print("\nFinal board:")
    print(game_state)
    
    winner = game_state.winner()
    if winner:
        print(f"\nPlayer {winner.value} wins")
    else:
        print("\nIt's a draw")

if __name__ == "__main__":
    main()
