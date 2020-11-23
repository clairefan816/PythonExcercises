from disk import Disk


class Chessboard:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = [[0] * self.column for i in range(self.row + 1)]
        # self.board_set = set()
        self.pix = 100

    def draw_board(self):
        stroke(0, 0, 255)
        strokeWeight(10)
        fill(209, 0)
        i = 0
        while i < self.row:
            j = 0
            while j < self.column:
                rect(j * self.pix, (i+1) * self.pix, self.pix, self.pix)
                j += 1
            i += 1

    def __str__(self):
        return "The current situation of chessboard is" + self.board_set

    def get_row_column(self, x):
        column = int(x // self.pix)
        row = self.get_vacant_row_by_column(column)
        return (row, column)

    def get_vacant_row_by_column(self, column):
        for row in range(self.row, 0, -1):
            if self.board[row][column] == 0:
                return row
        return 0

    def occupy(self, row, column, player_number):
        assert self.board[row][column] == 0
        self.board[row][column] = player_number

    def free(self, row, column):
        assert self.board[row][column] != 0
        self.board[row][column] = 0

    def row_column_to_xy(self, row, column):
        return (column * self.pix, row * self.pix)

    def check_board(self):
        for i in range(self.column):
            for j in range(1, self.row + 1):
                if self.board[j][i] == 0:
                    return True
        return False

    def check_win(self):
        # Check rows.
        for i in range(1, self.row + 1):
            count = 0
            last = 0
            for j in range(self.column):
                item = self.board[i][j]
                if item == last:
                    count += 1
                else:
                    count = 1
                    last = item
                if count == 4:
                    if last == 1:
                        return 'Player'
                    elif last == 2:
                        return 'Computer'
        # Check columns.
        for j in range(self.column):
            count = 0
            last = 0
            for i in range(1, self.row + 1):
                item = self.board[i][j]
                if item == last:
                    count += 1
                else:
                    count = 1
                    last = item
                if count == 4:
                    if last == 1:
                        return 'Player'
                    elif last == 2:
                        return 'Computer'
        # Check \ diag.
        for i, j in [(1, 0), (2, 0), (3, 0), (1, 1), (1, 2), (1, 3)]:
            distance = 0
            count = 0
            last = 0

            while distance < 7:
                if i + distance > self.row or j + distance >= self.column:
                    break
                item = self.board[i + distance][j + distance]
                if item == last:
                    count += 1
                else:
                    count = 1
                    last = item
                if count == 4:
                    if last == 1:
                        return 'Player'
                    elif last == 2:
                        return 'Computer'
                distance += 1

        # Check / diag.
        for i, j in [(1, 6), (2, 6), (3, 6), (1, 5), (1, 4), (1, 3)]:
            distance = 0
            count = 0
            last = 0

            while distance < 7:
                if i + distance > self.row or j - distance < 0:
                    break
                item = self.board[i + distance][j - distance]
                if item == last:
                    count += 1
                else:
                    count = 1
                    last = item
                if count == 4:
                    if last == 1:
                        return 'Player'
                    elif last == 2:
                        return 'Computer'
                distance += 1

        return None
