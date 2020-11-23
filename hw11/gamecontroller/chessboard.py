from disk import Disk


class Chessboard:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board_set = set()
        self.pix = 100

    def draw_board(self):
        stroke(0, 0, 255)
        strokeWeight(10)
        fill(209, 0)
        i = 0
        while i < self.row:
            j = 0
            while j < self.column:
                rect(self.pixel(j), self.pixel(i+1), self.pix, self.pix)
                j += 1
            i += 1

    def __str__(self):
        return "The current situation of chessboard is" + self.board_set

    def get_disk_location(self, x):
        column = x // self.pix
        for row in range(self.row, -1, -1):
            if (row, column) not in self.board_set:
                break
        if row > self.row or row < 1 or column > self.column or column < 0:
            return None
        return (row, column)

    def row_column_to_xy(self, row_column):
        return (row_column[1] * self.pix, row_column[0] * self.pix)

    def occupy(self, row_column):
        assert row_column not in self.board_set
        self.board_set.add(row_column)

    def pixel(self, column_or_row):
        return column_or_row * self.pix

    def check_board(self):
        if len(self.board_set) < self.row * self.column:
            return True
        else:
            return False
