import pandas as pd
import numpy as np
from app.core.settings import TEST_BOARD_PATH


def test_read_board():
    from app.core.core import _read_board_from_txt
    df = _read_board_from_txt(TEST_BOARD_PATH)
    assert df.size==81
    return df
    
def test_methods_last_hero():
    from app.workers import methods_last_hero
    df = test_read_board()

    # all test cases for test board
    indexes = [
        [0,1],
        [3,2],
        [5,0],
        [5,2],
        [7,0],
        [5,5],
        [3,7],
        [5,8]
    ]
    for nums in indexes:
        assert methods_last_hero(df, nums[0], nums[1]) == df[nums[1]][nums[0]]
    
    #more then one solution should return '0'
    assert methods_last_hero(df, row = 4, col = 3) == '0'

    # my testcases with custom boards
    board = '\
    000000000\
    000000000\
    080000000\
    000000000\
    400000000\
    000000000\
    650040000\
    142000000\
    730000040\
    '
    df = pd.DataFrame(np.array([list(row) for row in board.split()]))
    row, col = 7, 1
    assert methods_last_hero(df, row, col) == df[col][row]

    board = '\
    343000000\
    000000040\
    383000000\
    000000000\
    000000000\
    000000000\
    000040000\
    000000000\
    000000040\
    '
    df = pd.DataFrame(np.array([list(row) for row in board.split()]))
    row, col = 0, 1
    assert methods_last_hero(df, row, col) == df[col][row]

    board = '\
    300710000\
    000006031\
    100409026\
    630040007\
    000000000\
    780000050\
    460003000\
    275604000\
    003200068\
    '
    df = pd.DataFrame(np.array([list(row) for row in board.split()]))
    row, col = 0, 2
    assert methods_last_hero(df, row, col) == '6'

def test_methods_the_only_one_possible():
    board = '\
    306710000\
    000006031\
    150409026\
    630040007\
    000000000\
    780000050\
    460003000\
    275604000\
    003200068\
    '
    df = pd.DataFrame(np.array([list(row) for row in board.split()]))
    row, col = 2, 1
    from app.workers import methods_the_only_one_possible
    possibles = methods_the_only_one_possible(df, row, col)
    assert possibles == df[col][row]

