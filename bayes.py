import itertools
import matplotlib.pyplot as plt
from matplotlib import animation

import numpy as np


# data generator
def gen_data():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()

x_data, y_data = [], []


# init function, it will be called once only
def init():
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-2, 2.1)

    del x_data[:]
    del y_data[:]

    line.set_data(x_data, y_data)
    return line,


# main function
def run(data):
    t, y = data  # data from gen_data() function
    x_data.append(t)
    y_data.append(y)

    x_min, x_max = ax.get_xlim()

    # if the current x values same to the boundary of the x lime
    if t >= x_max:
        # x_lim gets updated
        ax.set_xlim(x_min, 2 * x_max)
        # drawing the new figure as the x_lim updated
        ax.figure.canvas.draw()

    # setting the new data
    line.set_data(x_data, y_data)
    return line,


# animation
ani = animation.FuncAnimation(fig, run, gen_data, interval=5, init_func=init)

plt.show()
