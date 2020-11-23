from disk import Disk
from chessboard import Chessboard

chessboard = Chessboard(2, 2)
count = 1
disks = []
my_disk = None
mouse_was_pressed = False

def setup():
    size(200, 300)
    ellipseMode(CORNER)
                
def draw():
    # draw the chessboard
    global mouse_was_pressed, count, my_disk, disks, chessboard
    background(209)
    if my_disk:
        my_disk.draw_disk()
    for disk in disks:
        disk.draw_disk()
    chessboard.draw_board()
    if all_disk_arrived():
        if not chessboard.check_board():
            print('GAME OVER!')
            noLoop()
        if mousePressed:
            # mouse_was_pressed = True
            location = chessboard.get_disk_location(mouseX)
            if location:
                x, y = chessboard.row_column_to_xy(location)
                my_disk = Disk(x, 0, x, y, location, count)
            else:
                my_disk = None
        else:
            # a mouse release event.
            # if mouse_was_pressed:
            #     mouse_was_pressed = False
                if my_disk:
                    my_disk.intact = False
                    count += 1
                    disks.append(my_disk)
                    chessboard.occupy(my_disk.row_column)
                    my_disk = None

def all_disk_arrived():
    for disk in disks:
        if not disk.arrived():
            return False
    return True
