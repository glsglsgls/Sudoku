import pandas as pd
from textwrap import wrap

board = "".join((
    '530070000',
    '600195000',
    '098000060',
    '800060003',
    '400803001',
    '700020006',
    '060000280',
    '000419005',
    '000080079'
))


class Row:
    def __init__(self, row_number: int):
        wrapped = wrap(board, 9)[row_number]
        self.data = pd.DataFrame(data=tuple(wrapped))


class Column:
    def __init__(self, col_number: int):
        wrapped = [str(val[col_number]) for val in wrap(board, 9)]
        self.data = pd.DataFrame(data=tuple(wrapped))


class Quad:
    def __init__(self, x: int, y: int):
        wrapped = wrap(board, 9)
        start_row = (x // 3) * 3
        start_col = (y // 3) * 3
        quad = "".join((val[start_col:start_col+3] for val in wrapped[start_row:start_row+3]))
        self.data = pd.DataFrame(data=tuple(quad))


def available(x, y):
    full = list(str(val) for val in range(1, 10))
    def find(obj):
        for digit in obj.data[1]:
            # Здесь проблема в цикле. Не видит цифры
            if digit in full:
                full.remove(digit)

    find(Row(x))
    find(Column(y))
    find(Quad(x, y))
    return full


wrapped_board = tuple(tuple(val) for val in wrap(board, 9))
for row in range(9):
    for col in range(9):
        if wrapped_board[row][col] == '0':
            a = available(row, col)
            print('')



