import numpy as np

board = "".join((
    '970000800',
    '000064020',
    '001500074',
    '043800090',
    '020309001',
    '008050040',
    '300400650',
    '700000032',
    '000080900'
))

# np_board = np.array(tuple("".join(board))).reshape(9, 9)

# print(np_board)


class Cell:
    row: int
    col: int
    content: int

    def __init__(self, row, col, content):
        self.row = row
        self.col = col
        self.content = content


class Quad:
    raw_numbers: str

    def __find_quad(self, pos):
        row, col = pos[0], pos[1]
        st_col, st_row = col // 3, row // 3
        end_col, end_row = st_col + 2, st_row + 2

        np_board = np.array(tuple("".join(self.raw_numbers))).reshape(9, 9)
        self.quad = np.array()

    def __init__(self, val, pos):


        from textwrap import wrap
        wrapped = [wrap(nums, 3) for nums in wrap(val, 9)]
        for i in range(1, 4):
            for j in range(1, 4):

                setattr(
                    self,
                    f"quad{i}{j}",
                    Quad("".join([wrapped[(i - 1) * 3][j - 1], wrapped[(i - 1) * 3 + 1][j - 1],
                                  wrapped[(i - 1) * 3 + 2][j - 1]]))
                )


        columns = []
        if 1<=col<=3:
            columns = [1, 2, 3]
        elif 4<=col<=6:
            columns = [1, 2, 3]
        elif 7<=col<=9:
            columns = [1, 2, 3]
        self.raw_numbers = val
        self.board()

    def __next__(self):
        return getattr(self, f'cell')

    def numbers(self):
        return sorted([int(num) for num in self.raw_numbers if int(num)])

    def missing(self):
        all_numbers = list(range(1, 10))
        for num in self.numbers():
            if num in all_numbers:
                all_numbers.remove(num)
        return sorted(all_numbers)

    def np_board(self):
        return np.array(tuple(self.raw_numbers)).reshape(3, 3)

    def board(self):
        count = 0
        for num in self.raw_numbers:
            row = count//3+1
            col = count%3+1
            setattr(self, f'cell{row}{col}', Cell(row,col, int(num)))
            count += 1

    def count_missing(self):
        return len(self.missing())


class Board:
    raw_board: str

    def __init__(self, val):
        self.raw_board = val
        '''if isinstance(val, tuple):
            val = "".join(val)
        if isinstance(val, str):
            from textwrap import wrap
            wrapped = [wrap(nums, 3) for nums in wrap(val, 9)]
            for i in range(1, 4):
                for j in range(1, 4):
                    setattr(
                        self,
                        f"quad{i}{j}",
                        Quad("".join([wrapped[(i-1)*3][j-1], wrapped[(i-1)*3+1][j-1], wrapped[(i-1)*3+2][j-1]]))
                    )
        '''

    def __str__(self):
        return str(self.raw_board)


b = Board(board)



class BaseSolver:
    board: Board
    quad: int
    pos: int

    def __init__(self, obj, quad, pos):
        self.board = obj
        self.quad = quad
        self.pos = pos

    def __possible(self):
        pass


class Loner(BaseSolver):
    def __init__(self, obj, quad, pos):
        super().__init__(obj, quad, pos)
        self.solver()

    def solver(self):
        quad = getattr(self.board, f'quad{self.quad}')
        for num in quad.raw_numbers:
            print('')


solve_it = Loner(b, 12, 9)



