from abc import abstractmethod, ABC
from random import random

from board import Board


class Heuristic(ABC):
    @abstractmethod
    def evaluate(self, board: Board):
        pass


class RandomHeuristic(Heuristic):
    def evaluate(self, board: Board):
        return random()
