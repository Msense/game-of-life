"""
rules in game-of-life

Copyright (C) 2019 Matthieu Senechal

Created by msenechal on 30/05/2019
"""
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt

from game.cell import *
from game.grid_np import Grid

matplotlib.use('MacOSX')

SIZE = 120
FIRST_CELLS = b_heptomino(50, 50) + r_pentomino(10, 10) + u_shape(80, 80)


start = Grid.create_with_cells(SIZE, FIRST_CELLS)

fig, ax = plt.subplots()
ax.set_axis_off()
cmap = plt.get_cmap('Accent_r')
matrix = ax.matshow(start, cmap=cmap)
cb = plt.colorbar(matrix)

fig.tight_layout()
cb.remove()
cnt = ax.text(1.0, 1.0, str(0),color='red', fontsize=20,
              verticalalignment='top', horizontalalignment='left',
              transform=ax.transAxes)
i = 0


def update_img(*args):
    global start, i
    start.iterate()
    matrix.set_array(start)
    cnt.set_text(str(i))
    i += 1


ani = animation.FuncAnimation(fig, update_img, interval=10)
ax.set_title("Iteration")

plt.show()
