from app.core.settings import QUAD_ROWS,QUAD_COLUMNS
from ctypes import ArgumentError
import numpy as np
import pandas as pd


def read_board_from_txt(path:str):
    with open(path,'r') as file:
        text = [list(row) for row in file.read().split()]
    global df 
    df = pd.DataFrame(np.array(text))
    return df

def get_quad(board:pd.DataFrame, position:int):
    if position not in range(1,10):
        raise Exception(ArgumentError(position, 'not in range 10'))
    
    quad = board.iloc[QUAD_ROWS[position]][QUAD_COLUMNS[position]]
    return quad