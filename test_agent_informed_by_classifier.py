from agents import ClassifierBasedAgent
from board import Board
from game import Game
from heuristics import IdealNeighborsHeuristic, MaxNeighborsHeuristic, MinNeighborsHeuristic
import pickle
import warnings
# to supress warnings related to classifier input not including feature names
warnings.filterwarnings("ignore", category=UserWarning)


def convert_board_to_multi_class_input(board: Board):
    input = []
    # add whether each cell is alive to the row
    for x in range(5):
        for y in range(5):
            input.append(board.is_live((x, y)))
    # play the board
    life_span_length = 0
    result_for_10_gen = Game(board, 10).play_without_agent(False, False)
    if result_for_10_gen > 0:
        life_span_length = 1
    result_for_50_gen = Game(board, 50).play_without_agent(False, False)
    if result_for_50_gen > 0:
        life_span_length = 2
    # append board features and heuristic values
    input.append(len(board.live_cells))
    input.append(IdealNeighborsHeuristic().evaluate(board))
    input.append(MaxNeighborsHeuristic().evaluate(board))
    input.append(MinNeighborsHeuristic().evaluate(board))
    return [input]


with open('trained_multi_class_classifier.pkl', 'rb') as f:
    multi_class = pickle.load(f)

multi_class_informed_agent = ClassifierBasedAgent(convert_board_to_multi_class_input, 2, multi_class)
board = Board(5, 5, {(2, 0), (2, 1), (2, 2), (2, 3)})
game_with_initially_infinite_config = Game(board.copy(), 50)
board = Board(5, 5, {(1, 1), (3, 2), (2, 3)})
game_with_initially_non_infinite_config = Game(board.copy(), 50)


game_with_initially_non_infinite_config.play_without_agent(with_sleeps=False)
game_with_initially_non_infinite_config.play_with_agent(multi_class_informed_agent, with_sleeps=False)
