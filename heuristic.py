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


class MaxNeighborsHeuristic(Heuristic):
    def evaluate(self, board: Board):
        total_neighbors = 0
        for x in range(board.width):
            for y in range(board.height):
                total_neighbors += len(board.get_live_neighbors((x, y)))
        return total_neighbors


class MinNeighborsHeuristic(Heuristic):
    def evaluate(self, board: Board):
        total_neighbors = 0
        for x in range(board.width):
            for y in range(board.height):
                total_neighbors += len(board.get_live_neighbors((x, y)))
        return 1/total_neighbors if total_neighbors > 0 else 0

class IdealNeighborsHeuristic(Heuristic):
    def evaluate(self, board: Board):
        cells_with_ideal_neighbors = 0
        for x in range(board.width):
            for y in range(board.height):
                neighbors = len(board.get_live_neighbors((x, y)))
                if neighbors == 2 or neighbors == 3:
                    cells_with_ideal_neighbors += 1

        return cells_with_ideal_neighbors
