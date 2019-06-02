"""
cell in game-of-life

Copyright (C) 2019 Matthieu Senechal

Created by msenechal on 31/05/2019
"""


def u_shape(x, y):
    return [
        (x, y),
        (x, y + 2),
        (x + 1, y),
        (x + 1, y + 2),
        (x + 2, y),
        (x + 2, y + 1),
        (x + 2, y + 2)
    ]


def r_pentomino(x, y):
    return [
        (x + 1, y + 1),
        (x + 2, y + 1),
        (x + 2, y + 2),
        (x + 3, y),
        (x + 3, y + 1)
    ]


def acorn(x, y):
    return [
        (x, y + 1),
        (x + 1, y + 3),
        (x + 2, y),
        (x + 2, y + 1),
        (x + 2, y + 4),
        (x + 2, y + 5),
        (x + 2, y + 6),
    ]


def b_heptomino(x, y):
    return [
        (x, y),
        (x, y + 2),
        (x, y + 3),
        (x + 1, y),
        (x + 1, y + 1),
        (x + 1, y + 2),
        (x + 2, y + 1),
    ]

