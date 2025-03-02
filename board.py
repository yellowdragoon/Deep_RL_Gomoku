from enum import Enum

class Player(Enum):
    NONE = 0
    BLACK = 1
    WHITE = 2

class GomokuBoard:
    def __init__(self, size=15):
        self.size = size
        self.board = [[Player.NONE] * size for _ in range(size)]
        self.side_to_move = Player.BLACK
        self.winner = None
        
    def generate_legal_moves(self) -> list:
        if self.is_game_over():
            return []
        
        # Generate moves
        moves = []
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] == Player.NONE:
                    moves.append((x, y, self.side_to_move))
                    
        return moves
    
    def is_game_over(self):
        return self.winner is not None

    def push(self, x, y, player):
        if self.board[y][x] != Player.NONE:
            raise ValueError("Invalid move, piece already placed there")
        
        self.board[y][x] = player
        
        # Horizontal
        for i in range(x-4, x+1):
            if i < 0 or i+4 > self.size:
                continue
            
            if all(self.board[y][i] == player for i in range(i, i+5)):
                self.winner = player
                return
            
        # Vertical
        for i in range(y-4, y+1):
            if y < 0 or y+4 > self.size:
                continue
            
            if all(self.board[i][x] == player for i in range(i, i+5)):
                self.winner = player
                return
            
        # Diagonal
        for i in range(-4, 1):
            if x+i < 0 or x+i+4 > self.size or y+i < 0 or y+i+4 > self.size:
                continue
            
            if all(self.board[y+i+j][x+i+j] == player for j in range(5)):
                self.winner = player
                return
            
        self.side_to_move = Player.BLACK if self.side_to_move == Player.WHITE else Player.WHITE
            
    def get(self, x, y):
        return self.board[y][x]

    def __str__(self):
        return '\n'.join(' '.join(str(cell.value) for cell in row) for row in self.board)

    def __repr__(self):
        return str(self)
