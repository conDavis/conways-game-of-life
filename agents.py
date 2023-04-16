from board import Board
from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def alter_board(self, board: Board):
        pass


class SimpleAgent(Agent):
    def __init__(self, heuristic=None, legal_num_of_board_alterations_per_turn=1):
        self.heuristic = heuristic  # not yet implemented
        self.legal_num_of_board_alterations_per_turn = legal_num_of_board_alterations_per_turn

    def alter_board(self, board: Board):
        """Make alterations to the given game of life board to elongate life based on the heuristic."""
        if board.is_dead((0, 0)):
            board.revive((0, 0))
        return board
