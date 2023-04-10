import time


class Board:
    """
    insert comment
    """

    def __init__(self, width=5, height=5, live_cells=[]):
        self.width = width
        self.height = height
        self.liveCells = live_cells

    def is_live(self, posn):
        return posn in self.liveCells

    def is_dead(self, posn):
        return posn not in self.liveCells \
            and posn[0] in range(0, self.width) \
            and posn[1] in range(0, self.height)


    def kill(self, posn):
        if posn in self.liveCells:
            self.liveCells.remove(posn)
        else:
            raise Exception('Unable to kill cell that isn\'t live')

    def revive(self, posn):
        if posn in self.liveCells:
            raise Exception('Cannot revive cell that is already alive.')
        else:
            self.liveCells.append(posn)

    def get_neighbors(self, posn):
        return [(posn[0] - 1, posn[1]),
                (posn[0], posn[1] - 1),
                (posn[0] - 1, posn[1] - 1),
                (posn[0] + 1, posn[1]),
                (posn[0], posn[1] + 1),
                (posn[0] + 1, posn[1] + 1),
                (posn[0] - 1, posn[1] + 1),
                (posn[0] + 1, posn[1] - 1)]

    def render(self):
        output = ''
        for row in range(0, self.height):
            for col in range(0, self.width):
                if (col, row) in self.liveCells:
                    output += "O"
                else:
                    output += "."
                output += " "
            output += '\n'

        print(output)


class Game:
    """
    insert comment
    """
    def __init__(self, board: Board, play_time=20):
        self.board = board
        self.play_time = play_time

    def play(self):
        print('Generation 0:')
        self.board.render()

        # alter the board with each tick as a new generation
        for tick in range(0, self.play_time):
            # creates a new board for the next generation
            next_board = Board(self.board.width, self.board.height, [])
            # iterating over each cell of the current generation
            for row in range(0, self.board.height):
                for col in range(0, self.board.width):
                    posn = (col, row)
                    neighbors = self.board.get_neighbors(posn)
                    live_neighbor_count = len(list(filter(lambda pos: self.board.is_live(pos), neighbors)))

                    # revives cells which are live and not in solitude or in overpopulation
                    if self.board.is_live(posn) and (live_neighbor_count == 2 or live_neighbor_count == 3):
                        next_board.revive(posn)
                    # revives empty cells with 3 live neighbors
                    elif self.board.is_dead(posn) and live_neighbor_count == 3:
                        next_board.revive(posn)

            print('Generation', tick + 1, ':')
            next_board.render()
            self.board = next_board
            time.sleep(1)

        # return and print the final score (number of live cells after play_time)
        score = len(self.board.liveCells)
        print('Number of live cells after', self.play_time, 'generations :', score)
        return score

