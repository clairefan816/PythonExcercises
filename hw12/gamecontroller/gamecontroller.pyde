from disk import Disk
from chessboard import Chessboard
from game_manager import GameManager
import score
import random

PLAYER_PLAY = 0
PLAYER_FLY = 1
AI_PLAY = 2
AI_FLY = 3
PLAYER_WON = 4

state = PLAYER_PLAY
gm = GameManager()
print("player first")


def setup():
    size(700, 700)
    ellipseMode(CORNER)


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message) 


def draw():
    # draw part
    global count, my_disk, disks, chessboard, state
    background(209)
    if gm.my_disk:
        gm.my_disk.draw_disk()
    for disk in gm.disks:
        disk.draw_disk()
    gm.chessboard.draw_board()
    
    if state == PLAYER_PLAY:
        if mousePressed:
            gm.prepare_to_drop()
        else:
            if gm.start_drop():
                state = PLAYER_FLY
    elif state == PLAYER_FLY:
        if gm.all_disk_arrived():
            winner = gm.chessboard.check_win()
            if winner:
                print (winner + 'wins!')
                state = PLAYER_WON
            else:
                state = AI_PLAY
    elif state == AI_PLAY:
        print("AI player")
        gm.computer_to_drop()
        state = AI_FLY
    elif state == AI_FLY: 
        if gm.all_disk_arrived():
            winner = gm.chessboard.check_win()
            if not winner:
                if not gm.chessboard.check_board():
                    print('GAME OVER!')
                    noLoop()
                else:
                    state = PLAYER_PLAY
                    print("player play")
            else:
                print (winner + 'wins!')
                noLoop()
    elif state == PLAYER_WON:
        answer = input('enter your name')
        if answer:
            record_player_win(answer)
        noLoop()


def record_player_win(player_name):
    dict = {}
    with open("scores.txt", "r") as f:
        read_data = f.readlines()
        for line in read_data:
            name, s = line.split()
            dict[name] = int(s)
    
    if player_name in dict:
        dict[player_name] += 1
    else:
        dict[player_name] = 1
     
    with open("scores.txt", "w") as f:
        sorted_result = sorted(dict, key = lambda x: x[1])
        for i in sorted_result:
            f.write('{} {}\n'.format(i, dict[i]))
            
