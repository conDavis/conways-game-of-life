# conways-game-of-life
Repository containing an implementation of Conway's game of life and several AI agents attempting to prolong life within the game. 

# Running Instructions
- Open a terminal within the project folder and run `python main.py` to compare the performance of our heuristic-based agents over 10 generations.

To run our classifiers:
- run `python train_and_test_bin_class.py` to see the results from our binary classifier which predicts whether a board will sustain infinite life or not.
- run `python train_and_test_multi_class.py` to see the results from our multiclass classifier which predicts which lifespan class a board will fall into. 

To run our classifier-based agent:
- run `python test_agent_informed_by_classifier.py` to see results of our agent's play on different board configurations over 50 generations.