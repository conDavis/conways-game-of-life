import csv
import random
import numpy as np
from board import Board
from game import Game
from heuristic import IdealNeighborsHeuristic, MaxNeighborsHeuristic, MinNeighborsHeuristic

header = []
# adding life at features for each posn

for x in range(0, 5):
    for y in range(0, 5):
        header.append(f"life_at_{x}_{y}")
header.append('num_alive')
header.append('ideal_neighbors_heuristic')
header.append('max_neighbors_heuristic')
header.append('min_neighbors_heuristic')
header.append('life_span_class') ## add comment here explaining the classes

## all possible posns -- created so that we can randomly choose from this bag
posns = []
for x in range(5):
    for y in range(5):
        posns.append((x, y))
posns = np.array(posns)
inds = list(range(5*5))

boards = set()
for board_index in range(30000):
    num_live = random.randint(0, len(inds))
    selected_inds = np.random.choice(inds, num_live, False)
    selected_posns = []
    for selected in selected_inds:
        selected_posns.append(tuple(posns[selected]))
    boards.add(Board(5, 5, set(selected_posns)))

print('num boards', len(boards))


with open('tern_training_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data, one row for each board
    for board in boards:
        row = []
        # add whether each cell is alive to the row
        for x in range(5):
            for y in range(5):
                row.append(board.is_live((x, y)))
        # play the board
        life_span_length = 0
        result_for_10_gen = Game(board, 10).play_without_agent(False, False)
        if result_for_10_gen > 0:
            life_span_length = 1
        result_for_50_gen = Game(board, 50).play_without_agent(False, False)
        if result_for_50_gen > 0:
            life_span_length = 2
        # append board features and heuristic values
        row.append(len(board.liveCells))
        row.append(IdealNeighborsHeuristic().evaluate(board))
        row.append(MaxNeighborsHeuristic().evaluate(board))
        row.append(MinNeighborsHeuristic().evaluate(board))
        row.append(life_span_length)
        print(row)
        writer.writerow(row)
