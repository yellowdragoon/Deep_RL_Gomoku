from typing import Tuple, List
import numpy as np

from board import Player

class gomokuEnv:
    def __init__(self):
        pass
    
    @staticmethod
    def state_to_input(state: Tuple[List[List[Player]], Player]) -> np.ndarray:
    
        # 1. Side to move encoding (1x15x15), 1 if it's black, 0 if it's white
        is_black_turn = np.ones((15, 15)) if state[1] is Player.BLACK else np.zeros((15, 15))

        # 2. Board encoding (2x15x15), 1 if there is a black/white stone, 0 otherwise
        black_board = np.zeros(15, 15)
        white_board = np.zeros(15, 15)
        for y in range(15):
            for x in range(15):
                if state[0][y][x] == Player.BLACK:
                    black_board[y][x] = True
                elif state[0][y][x] == Player.WHITE:
                    white_board[y][x] = True
                    
        combined_board = np.asarray([black_board, white_board])
        r = np.array([is_black_turn, *combined_board]).reshape((1, (15, 15, 3)))
        
        return r.astype(bool)
