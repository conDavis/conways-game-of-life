from board import Board
from abc import ABC, abstractmethod


class Agent(ABC):
    """
    An agent that plays Conway's game of life.
    """

    @abstractmethod
    def alter_board(self, board: Board):
        pass


class SimpleAgent(Agent):
    """
    The simplest form of agent, selecting its next move based on the evaluation of an inputted heuristic.
    """

    def __init__(self, heuristic=None, legal_num_of_board_alterations_per_turn=1):
        self.heuristic = heuristic  # not yet implemented
        self.legal_num_of_board_alterations_per_turn = legal_num_of_board_alterations_per_turn

    def alter_board(self, board: Board):
        """
        Make alterations to the given game of life board to elongate life based on the heuristic.
        """
        highest_heuristic = 0
        best_board = board
        for x in range(board.width):
            for y in range(board.height):
                new_board = board.copy()
                if board.is_dead((x, y)):
                    new_board.revive((x, y))
                elif board.is_live((x, y)):
                    new_board.kill((x, y))
                heuristic_val = self.heuristic.evaluate(new_board)
                if heuristic_val >= highest_heuristic:
                    best_board = new_board
                    highest_heuristic = heuristic_val
        return best_board
