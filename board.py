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
