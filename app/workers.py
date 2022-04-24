from ctypes import ArgumentError
from app.core import core


def read_board(path:str):
    if path[-3:] == 'txt':
        return core._read_board_from_txt(path)
    raise Exception(path)

def methods_last_hero(df, row:int, col:int):
    if not 0 <= row <= 8:
        raise ArgumentError('row should be in 0<=row<=8')
    if not 0 <= col <= 8:
        raise ArgumentError('column should be in 0<=column<=8')
    
    new_df = df.copy(deep=True)
    new_df[col][row] = '0'
    rows = core._get_neighbour(row)
    cols = core._get_neighbour(col)
    for x in core._get_possibles(new_df, row, col):
        """
        drop rows and columns, which already contain the "x" number
        if there is only one "0" left in quad after drop
         -> the current x number is the solution for this position
         """
        quad = core._get_quad(new_df, row, col)
        for num in cols:
            if str(x) in df[num].values:
                quad = quad.drop(num, axis=1)
        for num in rows:
            if str(x) in df.iloc[num].values:
                quad = quad.drop(num, axis=0)
        # 0 in quad.to_numpy() <-- search if df contains 0 
        if (quad == '0').sum(axis=1).sum() == 1:
            return str(x)
    return '0'

def methods_the_only_one_possible(df, row:int, col:int):
    new_df = df.copy(deep=True)
    new_df[col][row] = '0'
    possibles = core._get_possibles(new_df, row, col)
    if possibles.__len__() == 1:
        return str(possibles[0])
    return '0'