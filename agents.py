from board import Board
from abc import ABC, abstractmethod


class Agent(ABC):
    """
    An agent that plays Conway's game of life.
    """

    @abstractmethod
    def alter_board(self, board: Board):
        """
        Make alterations to the given Game of Life board in an attempt to elongate life.
        """
        pass


class SimpleAgent(Agent):
    """
    The simplest form of agent, selecting its next move based on the evaluation of a given heuristic.
    """

    def __init__(self, heuristic=None):
        self.heuristic = heuristic

    def alter_board(self, board: Board):
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


class ClassifierBasedAgent(Agent):
    """
     Agent selecting its next move based on the prediction of a given classifier.
     """
    def __init__(self, convert_board_to_classifier_input, index_of_infinite_life_class, classifier=None):
        self.classifier = classifier
        self.convert_board_to_classifier_input = convert_board_to_classifier_input
        self.index_of_infinite_life_class = index_of_infinite_life_class

    def alter_board(self, board: Board):
        """
        Make alterations to the given game of life board to elongate life based on the classifier's predictions.
        """
        highest_prob_infinite = 0
        best_board = board
        for x in range(board.width):
            for y in range(board.height):
                new_board = board.copy()
                if board.is_dead((x, y)):
                    new_board.revive((x, y))
                elif board.is_live((x, y)):
                    new_board.kill((x, y))

                classifier_infinite_life_prob = \
                    self.classifier.predict_proba(
                        self.convert_board_to_classifier_input(new_board))[0][self.index_of_infinite_life_class]

                if classifier_infinite_life_prob >= highest_prob_infinite:
                    best_board = new_board
                    highest_prob_infinite = classifier_infinite_life_prob
        return best_board
