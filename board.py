class Board:
    """
    Represents the board in Conway's game of life.
    """

    def __init__(self, width=5, height=5, live_cells=None):
        if live_cells is None:
            live_cells = set()
        self.width = width
        self.height = height
        self.live_cells = live_cells

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Board):
            if self.live_cells == other.live_cells:
                return self.width == other.width and self.height == other.height
        return False

    def __hash__(self):
        return hash(str(self.live_cells))

    def __str__(self):
        return f"| width: {self.width}, height: {self.height}, live_cells: {str(self.live_cells)} |"

    def is_live(self, posn):
        return posn in self.live_cells

    def is_dead(self, posn):
        return posn not in self.live_cells \
            and posn[0] in range(0, self.width) \
            and posn[1] in range(0, self.height)

    def kill(self, posn):
        if posn in self.live_cells:
            self.live_cells.remove(posn)
        else:
            raise Exception('Unable to kill cell that isn\'t live')

    def revive(self, posn):
        if posn in self.live_cells:
            raise Exception('Cannot revive cell that is already alive.')
        else:
            self.live_cells.add(posn)

    def get_live_neighbors(self, posn):
        neighbors = [(posn[0] - 1, posn[1]),
                     (posn[0], posn[1] - 1),
                     (posn[0] - 1, posn[1] - 1),
                     (posn[0] + 1, posn[1]),
                     (posn[0], posn[1] + 1),
                     (posn[0] + 1, posn[1] + 1),
                     (posn[0] - 1, posn[1] + 1),
                     (posn[0] + 1, posn[1] - 1)]
        return list(filter(lambda neighbor: self.is_live(neighbor), neighbors))

    def render(self):
        """
        Textually renders the current state of this board and prints it.
        """
        output = ''
        for row in range(0, self.height):
            for col in range(0, self.width):
                if (col, row) in self.live_cells:
                    output += "O"
                else:
                    output += "."
                output += " "
            output += '\n'

        print(output)

    def copy(self):
        return Board(self.width, self.height, self.live_cells.copy())
