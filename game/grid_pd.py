"""
grid in game-of-life

Copyright (C) 2019 Matthieu Senechal

Created by msenechal on 31/05/2019
"""
import pandas as pd


class Grid(pd.DataFrame):
    def __init__(self, size, starting_cells):
        super().__init__([[0] * size] * size)
        self.dimension = size
        self._initialisation(starting_cells)

    def _initialisation(self, starting_cells):
        for cell in starting_cells:
            self.iat[cell[0], cell[1]] = 1

    @staticmethod
    def _up(grid, size):
        return pd.concat([grid.iloc[1:, ], pd.DataFrame([[0] * size])], ignore_index=True)

    @staticmethod
    def _down(grid, size):
        return pd.concat([pd.DataFrame([[0] * size]), grid.iloc[:-1, ]], ignore_index=True)

    @staticmethod
    def _left(grid, size):
        tmp = pd.concat([grid.loc[:, 1:], pd.DataFrame([[0]] * size)], axis=1)
        tmp.columns = grid.columns
        return tmp

    @staticmethod
    def _right(grid, size):
        tmp = pd.concat([pd.DataFrame([[0]] * size), grid.iloc[:, :-1]], axis=1)
        tmp.columns = grid.columns
        return tmp

    def _count_neighbours(self):
        up_move = self._up(self, self.dimension)
        up_left_move = self._up(self._left(self, self.dimension), self.dimension)
        up_right_move = self._up(self._right(self, self.dimension), self.dimension)
        right_move = self._right(self, self.dimension)
        down_right_move = self._down(self._right(self, self.dimension), self.dimension)
        down_move = self._down(self, self.dimension)
        down_left_move = self._down(self._left(self, self.dimension), self.dimension)
        left_move = self._left(self, self.dimension)

        count = up_move + \
            up_left_move + \
            up_right_move + \
            right_move + \
            down_right_move + \
            down_move + \
            down_left_move + \
            left_move

        return count

    @staticmethod
    def rules(cell, count):
        return count == 3 or cell and count == 2

    @staticmethod
    def _rule_1(count):
        return int(count == 3)

    @staticmethod
    def _rule_2(count):
        return int(count == 2)

    @staticmethod
    def _int_bool(element: int):
        return int(bool(element))

    def iterate(self):
        count = self._count_neighbours()
        count_tmp = count.copy()
        count_1 = count_tmp.applymap(self._rule_1)
        count_2 = count.applymap(self._rule_2)
        tmp = count_1 + count_2 * self
        tmp.applymap(self._int_bool)
        self.update(tmp)
