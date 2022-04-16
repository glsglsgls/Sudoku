from cgi import test
from app import __version__
from app.core.settings import TEST_BOARD_PATH


def test_version():
    assert __version__ == '0.1.0'


def test_read_board():
    from app.workers import read_board_from_txt
    assert read_board_from_txt(TEST_BOARD_PATH).size==81

def test_get_quad():
    test_read_board()
    from app.workers import get_quad, df
    for pos in range(1,10):
        assert get_quad(df,pos).size==9

def test_methods_last_hero():
    test_read_board()
    from app.workers import get_quad, df

