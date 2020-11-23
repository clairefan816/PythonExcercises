from chessboard import Chessboard

chessboard_a = Chessboard(2, 2)
chessboard_b = Chessboard(0, 0)
chessboard_c = Chessboard(1, 4)


def test_constructor():
    """Test the constructor"""
    assert chessboard_a.board == [[0, 0], [0, 0], [0, 0]]
    assert chessboard_b.board == [[]]
    assert chessboard_c.board == [[0, 0, 0, 0], [0, 0, 0, 0]]


def test_get_row_column():
    """Test the method of getting spot"""
    chessboard_a.get_row_column(50)
    assert chessboard_a.get_row_column(50) == (2, 0)
    assert chessboard_a.get_row_column(150) == (2, 1)


def test_get_vacant_row_by_column():
    """Test the method of checking the vacant spot"""
    assert chessboard_a.get_vacant_row_by_column(0) == 2


def test_occupy():
    """Test the method of occupying the spot"""
    chessboard_a.occupy(1, 1, 1)
    assert chessboard_a.board[1][1] == 1
    chessboard_a.occupy(1, 0, 2)
    assert chessboard_a.board[1][0] == 2


def test_free():
    """Test the method of releasing the spot"""
    chessboard_a.free(1, 1)
    assert chessboard_a.board[1][1] == 0


def test_check_board():
    """Test the method of peeking the board"""
    chessboard_a.board[1][0] = 1
    chessboard_a.board[1][1] = 2
    chessboard_a.board[2][0] = 0
    chessboard_a.board[2][1] = 0
    assert chessboard_a.check_board() is True
    chessboard_a.occupy(2, 0, 1)
    chessboard_a.occupy(2, 1, 2)
    assert chessboard_a.check_board() is False


def test_check_win():
    """Test the method of finding the winner"""
    chessboard_c.board = [[0, 0, 0, 0], [1, 1, 1, 1]]
    assert "player"
    chessboard_c.board = [[0, 0, 0, 0], [2, 2, 2, 2]]
    assert "computer"
