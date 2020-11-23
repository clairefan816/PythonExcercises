from chessboard import Chessboard
import random

# middle column gets the highest point
COLUMN_SCORE = [1, 2, 3, 4, 3, 2, 1]


def ai_play(chessboard):
    max_score = - (2 ** 63)
    max_column = - 1
    for column in range(7):
        row = chessboard.get_vacant_row_by_column(column)
        if not row:
            continue
        score = compute_score(chessboard, row, column)
        if score > max_score:
            max_score = score
            max_column = column
    return max_column * 100 + 50


# Computes a score of the chessboard if AI plays next disk at (row, column)
def compute_score(chessboard, row, column):
    sum = COLUMN_SCORE[column]
    all_list = get_all_list(chessboard, row, column)
    for l in all_list:
        sum += list_score(l)
    return sum


def list_score(l):
    score = 0
    for n in range(len(l) - 1):
        if l[n:n+2] == [2, 2]:
            score += 50
    for n in range(len(l) - 2):
        if l[n:n+3] == [1, 2, 1]:
            score -= 100
    for n in range(len(l) - 3):
        if l[n:n+4] == [1, 2, 2, 1]:
            score -= 100
        elif l[n:n+4] == [2, 1, 1, 0] or l[n:n+4] == [0, 1, 1, 2]:
            score += 500
        elif l[n:n+4] == [1, 1, 1, 2] or l[n:n+4] == [2, 1, 1, 1]:
            score += 9000
        elif l[n:n+4] == [2, 2, 2, 2]:
            score += 10000
        elif l[n:n+4] == [0, 2, 2, 2] or l[n:n+4] == [2, 2, 2, 0]:
            score += 800
    for n in range(len(l) - 4):
        if l[n:n+5] == [0, 2, 2, 2, 0]:
            score += 900
        elif l[n:n+5] == [1, 2, 2, 2, 1]:
            score -= 100
    return score


def get_all_list(chessboard, row, column):
    chessboard.occupy(row, column, 2)
    all_list = []
    for i in range(1, 7):
        all_list.append([chessboard.board[i][j] for j in range(7)])
    for j in range(7):
        all_list.append([chessboard.board[i][j] for i in range(1, 7)])
    for i, j in [(1, 0), (2, 0), (3, 0), (1, 1), (1, 2), (1, 3)]:
        distance = 0
        list_one = []
        while distance < 7:
            if i + distance > 6 or j + distance >= 6:
                break
            list_one.append(chessboard.board[i + distance][j + distance])
            distance += 1
        all_list.append(list_one)
    # Check / diag.
    for i, j in [(1, 6), (2, 6), (3, 6), (1, 5), (1, 4), (1, 3)]:
        distance = 0
        list_two = []
        while distance < 7:
            if i + distance > 6 or j - distance < 0:
                break
            list_two.append(chessboard.board[i + distance][j - distance])
            distance += 1
        all_list.append(list_two)
    chessboard.free(row, column)
    return all_list
