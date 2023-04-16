from game import Board
from game import Game
from agents import SimpleAgent
from heuristic import RandomHeuristic, MaxNeighborsHeuristic, MinNeighborsHeuristic, IdealNeighborsHeuristic

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board(5, 5, [(2, 0), (2, 1), (2, 2), (2, 3)])
    game = Game(board.copy(), 10)
    #game.play_without_agent()
    game.play_with_agent(SimpleAgent(RandomHeuristic()))

    game = Game(board.copy(), 10)
    game.play_with_agent(SimpleAgent(MaxNeighborsHeuristic()))

    game = Game(board.copy(), 10)
    game.play_with_agent(SimpleAgent(MinNeighborsHeuristic()))

    game = Game(board.copy(), 10)
    game.play_with_agent(SimpleAgent(IdealNeighborsHeuristic()))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
