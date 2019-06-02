"""
grid_np in game-of-life

Copyright (C) 2019 Matthieu Senechal

Created by msenechal on 31/05/2019
"""
import numpy as np


class Grid(np.ndarray):
    def __new__(cls, input_array):
        if len(input_array[0]) != len(input_array[1]):
            raise ValueError("The input array must be a square")
        obj = np.asarray(input_array, dtype=int).view(cls)
        return obj

    @classmethod
    def create_empty(cls, dimension):
        return cls(np.zeros(shape=(dimension, dimension), dtype=int))

    @classmethod
    def create_with_cells(cls, dimension, starting_cells):
        obj = cls.create_empty(dimension)
        obj.set_cells(starting_cells)
        return obj

    def set_cells(self, starting_cells):
        if starting_cells is None:
            return None
        for cell in starting_cells:
            self[cell[0], cell[1]] = 1

    def _up(self):
        new_line = np.zeros(shape=(1, self.shape[0]), dtype=int)
        return Grid(np.concatenate((self[1:, ], new_line)))

    def _down(self):
        new_line = np.zeros(shape=(1, self.shape[0]), dtype=int)
        return Grid(np.concatenate((new_line, self[:-1, ])))

    def _left(self):
        new_column = np.zeros(shape=(self.shape[0], 1), dtype=int)
        return Grid(np.concatenate((self[:, 1:], new_column), axis=1))

    def _right(self):
        new_column = np.zeros(shape=(self.shape[0], 1), dtype=int)
        return Grid(np.concatenate((new_column, self[:, :-1]), axis=1))

    def _count_neighbours(self):
        up_move = self._up()
        up_left_move = self._up()._left()
        up_right_move = self._up()._right()
        right_move = self._right()
        down_right_move = self._down()._right()
        down_move = self._down()
        down_left_move = self._down()._left()
        left_move = self._left()

        count = up_move + \
            up_left_move + \
            up_right_move + \
            right_move + \
            down_right_move + \
            down_move + \
            down_left_move + \
            left_move

        return count

    def iterate(self):
        count = self._count_neighbours()
        mask = Grid(np.logical_or(count == 3, np.logical_and(self, count == 2)))
        self[::1] = 0
        np.putmask(self, mask, 1)
