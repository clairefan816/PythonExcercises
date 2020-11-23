import score
from chessboard import Chessboard


cb = Chessboard(6, 7)
cb.board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, 1, 0, 0, 0],
    [0, 0, 1, 2, 1, 0, 0],
    [0, 0, 2, 1, 2, 0, 0]]


def test_get_all_list():

    all_list = score.get_all_list(cb, 6, 5)

    assert len(all_list) == 25
    assert all_list == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
        [0, 0, 1, 2, 1, 0, 0],
        [0, 0, 2, 1, 2, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 1, 2],
        [0, 0, 0, 1, 2, 1],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 2],
        [0, 0, 2, 2, 2],
        [0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 2, 2],
        [0, 0, 1, 1],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0]]


def test_list_score():
    assert score.list_score([0, 0, 0, 0, 0, 0, 0]) == 0
    assert score.list_score([2, 2, 2, 2, 0, 0, 0]) == 10950
    assert score.list_score([0, 0, 2, 2, 2, 2, 0]) == 11750
    assert score.list_score([2, 2, 2, 0, 0, 0, 0]) == 900
    assert score.list_score([0, 0, 2, 2, 2, 0, 0]) == 2600
    assert score.list_score([0, 2, 2, 0, 0, 0, 0]) == 50
    assert score.list_score([0, 2, 1, 1, 2, 0, 0]) == 0
    assert score.list_score([0, 0, 1, 1, 2, 0, 0]) == 500
    assert score.list_score([0, 2, 1, 1, 1, 2, 0]) == 18000


def test_compute_score():
    s1 = score.compute_score(cb, 6, 0)
    s2 = score.compute_score(cb, 6, 1)
    s3 = score.compute_score(cb, 2, 2)
    s4 = score.compute_score(cb, 3, 3)
    s5 = score.compute_score(cb, 4, 4)
    s6 = score.compute_score(cb, 6, 5)
    s7 = score.compute_score(cb, 6, 6)
    assert s1 == 651
    assert s2 == 1202
    assert s3 == 653
    assert s4 == 704
    assert s5 == 1503
    assert s6 == 9702
    assert s7 == 651


def test_ai_play():
    x = score.ai_play(cb)
    assert x == 550
