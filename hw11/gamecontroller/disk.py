class Disk:
    def __init__(self, x, y, target_x, target_y, row_column, count):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.row_column = row_column
        self.radius = 50
        self.diam = self.radius*2
        self.count = count
        self.intact = True

    def draw_disk(self):
        noStroke()
        self.disk_flying()
        if self.count % 2 == 0:
            fill(255, 0, 0)
            ellipse(self.x, self.y, self.diam, self.diam)
        else:
            fill(255, 255, 0)
            ellipse(self.x, self.y, self.diam, self.diam)

    def disk_flying(self):
        if not self.intact:
            if self.y != self.target_y:
                self.y += 10
        else:
            pass

    def arrived(self):
        return self.x == self.target_x and self.y == self.target_y
