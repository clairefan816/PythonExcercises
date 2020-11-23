from chessboard import Chessboard
from disk import Disk
import score


class GameManager:
    def __init__(self):
        self.count = 1
        self.disks = []
        self.my_disk = None
        self.chessboard = Chessboard(6, 7)

    def prepare_to_drop(self):
        # called when mousePressed
        row, column = self.chessboard.get_row_column(mouseX)
        if row:
            x, y = self.chessboard.row_column_to_xy(row, column)
            self.my_disk = Disk(x, 0, x, y, row, column, self.count)
        else:
            self.my_disk = None

    def start_drop(self):
        # called when mouseReleased
        if self.my_disk:
            self.my_disk.intact = False
            self.count += 1
            self.disks.append(self.my_disk)
            self.chessboard.occupy(self.my_disk.row, self.my_disk.column, 1)
            self.my_disk = None
            return True
        return False

    def computer_to_drop(self):
        aiX = score.ai_play(self.chessboard)
        row, column = self.chessboard.get_row_column(aiX)
        x, y = self.chessboard.row_column_to_xy(row, column)
        ai_disk = Disk(x, 0, x, y, row, column, self.count)
        ai_disk.intact = False
        self.count += 1
        self.disks.append(ai_disk)
        self.chessboard.occupy(row, column, 2)

    def all_disk_arrived(self):
        for self.disk in self.disks:
            if not self.disk.arrived():
                return False
        return True
