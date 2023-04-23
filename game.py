import time
from agents import Agent
from board import Board


class Game:
    """
    Represent an instance of Conway's Game of Life.
    Produces a generation once every tick in play_time and alters this game's board accordingly.
    Playable with interference from an agent, meaning after every generation (excluding the last)
    an agent is allowed to alter one cell of this game's board.
    """

    def __init__(self, board: Board, play_time=20):
        self.board = board
        self.play_time = play_time

    def produce_next_gen(self):
        # creates a new board for the next generation
        next_board = Board(self.board.width, self.board.height)
        # iterating over each cell of the current generation
        for row in range(0, self.board.height):
            for col in range(0, self.board.width):
                posn = (col, row)
                live_neighbor_count = len(self.board.get_live_neighbors(posn))

                # revives cells which are live and not in solitude or in overpopulation
                if self.board.is_live(posn) and (live_neighbor_count == 2 or live_neighbor_count == 3):
                    next_board.revive(posn)
                # revives empty cells with 3 live neighbors
                elif self.board.is_dead(posn) and live_neighbor_count == 3:
                    next_board.revive(posn)

        self.board = next_board
        return next_board

    def play_without_agent(self, with_sleeps=True, with_rendering=True):
        """This function could be useful for evaluating agent performance in elongating life in comparison."""
        if with_rendering:
            print('Generation 0:')
            self.board.render()
        # preserving initial board
        init_board = self.board.copy()

        # alter the board with each tick as a new generation
        for tick in range(0, self.play_time):
            self.produce_next_gen()
            if with_rendering:
                print('Generation', tick + 1, ':')
                self.board.render()
            if with_sleeps:
                time.sleep(1)

        # return and print the final score (number of live cells after play_time)
        score = len(self.board.live_cells)
        print('Number of live cells after', self.play_time, 'generations :', score)
        self.board = init_board
        return score

    def play_with_agent(self, agent: Agent, with_sleeps=True, with_rendering=True):
        if with_rendering:
            print('Generation 0:')
            self.board.render()
        if with_sleeps:
            time.sleep(1)
        init_board = self.board.copy()  # preserving initial board
        self.board = agent.alter_board(board=self.board)
        if with_rendering:
            print('Generation 0 after agent move:')
            self.board.render()
        if with_sleeps:
            time.sleep(1)

        # produce a new generation and allow the agent to alter the board for each tick
        for tick in range(0, self.play_time):
            self.produce_next_gen()
            if with_rendering:
                print('Generation', tick + 1, ':')
                self.board.render()
            if with_sleeps:
                time.sleep(1)

            # if this is not the last generation allow the agent to alter the board before the next
            if tick != self.play_time - 1:
                self.board = agent.alter_board(board=self.board)
                if with_rendering:
                    print('Generation', tick + 1, 'after agent move:')
                    self.board.render()
                if with_sleeps:
                    time.sleep(1)

        # return and print the final score (number of live cells after play_time)
        score = len(self.board.live_cells)
        print('Number of live cells after', self.play_time, 'generations :', score)
        # resetting board
        self.board = init_board
        return score
