import numpy as np
import pandas as pd
from ctypes import ArgumentError

def _read_board_from_txt(path:str):
    with open(path,'r') as file:
        text = [list(row) for row in file.read().split()]
    return pd.DataFrame(np.array(text))

def _get_quad(board:pd.DataFrame, row:int, col:int):
    rows=list(_get_neighbour(row)); rows.append(row); rows.sort()
    cols=list(_get_neighbour(col)); cols.append(col); cols.sort()

    if row not in range(9):
        raise Exception(ArgumentError('value not in range "0-8"'))
    
    quad = board.iloc[rows][cols]
    return quad

def _get_possibles(df:pd.DataFrame, row:int, col:int) -> list:
    possible_values = []
    quad = _get_quad(df, row, col)
    whole_col = df[col]
    whole_row = df.iloc[row]
    for item in range(1,10):
        if str(item) not in quad.values \
        and str(item) not in whole_col.values \
        and str(item) not in whole_row.values:
            try:
                possible_values.append(item)
            except: pass
    return possible_values
    

def _get_neighbour(num: int) -> int:
    st = num // 3 * 3
    if st == num:
        return st+1, st+2
    elif num == st + 1:
        return st, st+2
    elif num == st + 2:
        return st, st+1
    else:
        raise Exception  