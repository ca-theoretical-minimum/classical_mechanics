from typing import Tuple

import numpy as np

from src.utils.plotting import plot_ode

Condition = Tuple[float, float, float, float]


def particle_on_a_carousel(
    conditions: Condition,
    t: float,
    m: float,
    w: float
) -> Condition:
    """
    Calculate one step for particle motion on a carousel.

    :param conditions: [x, xd, y, yd]
    :param t: Time (unused).
    :param m: Mass of particle.
    :param w: Angular velocity of carousel.

    :return:
        Derivative estimates for each condition.
    """

    x, xd, y, yd = conditions

    xdd = w ** 2 * m * x - m * w * yd

    ydd = w ** 2 * m * y + m * w * xd

    return xd, xdd, yd, ydd


if __name__ == '__main__':

    times = np.linspace(0, 20, 1000)

    system_params = {
        'm': 1,
        'w': 0.5,
    }

    plot_ode(
        particle_on_a_carousel,
        [-100, 1, -100, 1],
        times,
        system_params,
        xlim=200,
        ylim=(-1000, -100),
        save='imgs/3_particle_on_a_carousel.mp4',
    )
