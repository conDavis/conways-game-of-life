import time


class Board:
    """
    insert comment
    """

    def __init__(self, width, height, unused_cells=[], live_cells=[]):
        self.width = width
        self.height = height
        self.unusedCells = unused_cells
        self.liveCells = live_cells

    def is_live(self, posn):
        return posn in self.liveCells

    def is_dead(self, posn):
        return posn not in self.liveCells \
            and posn not in self.unusedCells \
            and posn[0] in range(0, self.width) \
            and posn[1] in range(0, self.height)


    def is_unused(self, posn):
        return posn in self.unusedCells

    def kill(self, posn):
        if posn in self.liveCells:
            self.liveCells.remove(posn)
        elif posn in self.unusedCells:
            raise Exception('Unable to kill cell that is unused')
        else:
            raise Exception('Unable to kill cell that isn\'t live')

    def revive(self, posn):
        if posn in self.unusedCells:
            raise Exception('Unable to revive cell that is unused')
        elif posn in self.liveCells:
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
                elif (col, row) in self.unusedCells:
                    output += " "
                else:
                    output += "X"
                output += " "
            output += '\n'

        print(output)


class Game:
    """
    insert comment
    """
    def __init__(self, board: Board, playTime=20):
        self.board = board
        self.playTime = playTime

    def play(self):
        self.board.render()
        for tick in range(0, self.playTime):
            next_board = Board(self.board.width, self.board.height, self.board.unusedCells, [])
            for row in range(0, self.board.height):
                for col in range(0, self.board.width):
                    posn = (col, row)
                    neighbors = self.board.get_neighbors(posn)
                    live_neighbor_count = len(list(filter(lambda pos: self.board.is_live(pos), neighbors)))
                    if self.board.is_live(posn) and (live_neighbor_count == 2 or live_neighbor_count == 3):
                        next_board.revive(posn)
                    # revives empty cells with 3 live neighbors
                    elif self.board.is_dead(posn) and live_neighbor_count == 3:
                        next_board.revive(posn)
            next_board.render()
            self.board = next_board
            time.sleep(1)
