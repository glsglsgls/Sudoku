from pandas import DataFrame
import pandas as pd
import numpy as np
from app.core.settings import TEST_BOARD_PATH


def test_read_board_from_txt():
    from app.core.core import _read_board_from_txt
    df = _read_board_from_txt(TEST_BOARD_PATH)
    assert df.size==81
    return df

def test_get_quad():
    df = test_read_board_from_txt()
    from app.core.core import _get_quad
    a = _get_quad(df, 7, 1).reset_index(drop=True)
    b=pd.DataFrame([['6','5','0'],['1','4','0'],['7','3','0']])
    assert a.equals(b)

def test_get_possibles():
    df = test_read_board_from_txt()
    from app.core.core import _get_possibles
    assert _get_possibles(df, row=3, col=0) == [2, 5]
    assert _get_possibles(df, row=4, col=4) == [2, 6, 8]
    
def test_get_neighbour():
    from app.core.core import _get_neighbour as gnb
    assert gnb(0) == (1, 2)
    assert gnb(2) == (0, 1)
    assert gnb(3) == (4, 5)
    assert gnb(7) == (6, 8)
    assert gnb(8) == (6, 7)