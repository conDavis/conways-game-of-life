import csv
import random
import numpy as np
from board import Board
from game import Game
from heuristics import IdealNeighborsHeuristic, MaxNeighborsHeuristic, MinNeighborsHeuristic, RandomHeuristic
from agents import SimpleAgent

header = ['board_representation',
          'random_agent_final_score_20_gen',
          'random_agent_final_score_50_gen',
          'maximizing_neighbors_agent_final_score_20_gen',
          'maximizing_neighbors_agent_final_score_50_gen',
          'minimizing_neighbors_agent_final_score_20_gen',
          'minimizing_neighbors_agent_final_score_50_gen',
          'idealizing_neighbors_agent_final_score_20_gen',
          'idealizing_neighbors_agent_final_score_50_gen',
          'without_agent_final_score_20_gen',
          'without_agent_final_score_50_gen',
          'is_infinite_without_interference']

# all possible posns -- created so that we can randomly choose from this bag
posns = []
for x in range(5):
    for y in range(5):
        posns.append((x, y))
posns = np.array(posns)
inds = list(range(5*5))

boards = set()
print('Generating random board configurations ...')
while len(boards) < 10000:
    num_live = random.randint(0, len(inds))
    selected_inds = np.random.choice(inds, num_live, False)
    selected_posns = []
    for selected in selected_inds:
        selected_posns.append(tuple(posns[selected]))
    boards.add(Board(5, 5, set(selected_posns)))
print('Boards generated:', len(boards))


with open('heuristic_evaluation_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # create agents with heuristics to test on
    agent_using_rand_heuristics = SimpleAgent(RandomHeuristic())
    agent_using_max_neighbors_heuristics = SimpleAgent(MaxNeighborsHeuristic())
    agent_using_min_neighbors_heuristics = SimpleAgent(MinNeighborsHeuristic())
    agent_using_ideal_neighbors_heuristics = SimpleAgent(IdealNeighborsHeuristic())

    # write the data, one row for each board
    print('Evaluating board configurations and writing results to CSV ...')
    for board in boards:
        row = [str(board)]
        # play the board with each agent and without an agent
        random_heuristic_result = Game(board, 20).play_with_agent(agent_using_rand_heuristics, False, False)
        row.append(random_heuristic_result)

        random_heuristic_result = Game(board, 50).play_with_agent(agent_using_rand_heuristics, False, False)
        row.append(random_heuristic_result)

        max_neighbors_heuristic_result = Game(board, 20).play_with_agent(agent_using_max_neighbors_heuristics, False, False)
        row.append(max_neighbors_heuristic_result)

        max_neighbors_heuristic_result = Game(board, 50).play_with_agent(agent_using_max_neighbors_heuristics, False,
                                                                         False)
        row.append(max_neighbors_heuristic_result)

        min_neighbors_heuristic_result = Game(board, 20).play_with_agent(agent_using_min_neighbors_heuristics, False, False)
        row.append(min_neighbors_heuristic_result)

        min_neighbors_heuristic_result = Game(board, 50).play_with_agent(agent_using_min_neighbors_heuristics, False,
                                                                         False)
        row.append(min_neighbors_heuristic_result)

        ideal_neighbors_heuristic_result = Game(board, 20).play_with_agent(agent_using_ideal_neighbors_heuristics, False, False)
        row.append(ideal_neighbors_heuristic_result)

        ideal_neighbors_heuristic_result = Game(board, 50).play_with_agent(agent_using_ideal_neighbors_heuristics,
                                                                           False, False)
        row.append(ideal_neighbors_heuristic_result)

        game_result_without_agent = Game(board, 20).play_without_agent(False, False)
        row.append(game_result_without_agent)

        game_result_without_agent = Game(board, 50).play_without_agent(False, False)
        row.append(game_result_without_agent)

        is_infinite = game_result_without_agent > 0
        row.append(is_infinite)

        writer.writerow(row)
