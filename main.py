from game import Board
from game import Game
from agents import SimpleAgent


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board(5, 5, [(2, 0), (2, 1), (2, 2), (2, 3)])
    game = Game(board, 10)
    game.play_without_agent()
    game.play_with_agent(SimpleAgent())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
