import functools
from numbers import Number
from typing import Callable, Iterable, Union, Tuple

import numpy as np
import sympy
from matplotlib import pyplot as plt, animation
from matplotlib.animation import FuncAnimation
from numpy import sin, cos
from scipy.integrate import odeint


mpl_lim = Union[float, Tuple[float, float]]


def plot_ode(
    func: Callable,
    initial_conditions: Iterable,
    times: np.ndarray,
    system_params: dict,
    show: bool = True,
    save: str = '',
    xlim: mpl_lim = 10,
    ylim: mpl_lim = 10,
):
    """
    Animate the coupled pendulums.

    Args:
        func: Function to be integrated.
        initial_conditions: Initial conditions for seeding integral.
        times: Times to evaluate equations of motion.
        system_params: Physical parameters of the system.
        show: Display trajectory animation.
        save: Filepath to save trajectory animation.
        xlim: For plotting.
        ylim: For plotting.
    """

    pend_func = functools.partial(func, **system_params)

    x, xd, y, yd = odeint(pend_func, initial_conditions, times).T

    if isinstance(xlim, (int, float)):
        xlim = -xlim, xlim

    if isinstance(ylim, (int, float)):
        ylim = -ylim, ylim

    m = (x > xlim[0]) & (x < xlim[1])
    m &= (y > ylim[0]) & (y < ylim[1])

    x, y = x[m], y[m]

    fig, ax = plt.subplots()

    ln, = ax.plot([], [], 'o')

    def init():

        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ln.set_data([], [])
        return ln,

    def update(vals):

        ln.set_data(vals[:1], vals[1:])
        return ln,

    import ipdb; ipdb.set_trace()

    frames = np.stack([x, y], axis=-1)

    ani = FuncAnimation(fig, update, init_func=init, frames=frames, blit=True, interval=25, repeat=False)

    if save:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=40, metadata=dict(artist='Me'), bitrate=1800)

        ani.save(save, writer=writer)

    if show:
        plt.show()
