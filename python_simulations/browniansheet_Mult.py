#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    python_simulations.browniansheet_Mult
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This is a simulation for Brownian Sheet....

    :copyright: (c) 2022 by Nick Eisenberg <nickeisenberg@gmail.com>.
    :license: LICENSE_NAME, see LICENSE for more details.
    :created at Wed 02 Mar 2022 10:55:11 AM CST
"""

# A simulation of a Brownian sheet though multiplication of independent Brownian motions

import numpy as np
import matplotlib.pyplot as plt
# import time
# import math
from mpl_toolkits.mplot3d.axes3d import Axes3D


def BrownianSheet(t, nt, x, nx):
    """TODO: Docstring for BrownianSheet.
    :1: TODO
    :returns: TODO
    """
    delta_t = t / nt
    delta_x = x / nx
    # Create the Brownian sheet noise
    W_tx = np.zeros((nx + 1, nt + 1))
    for x in range(nx):
        for t in range(nt):
            dW = np.random.normal(0, delta_t * delta_x, size=1)
            W_tx[x + 1, t + 1] = W_tx[x, t + 1] + W_tx[x + 1, t] - W_tx[x, t] + dW[0]
    return W_tx


def BrownianSheetMovie():
    # Set the time and space intervals. Choose number of partitions of each.
    # Time
    t = 5
    nt = 100

    # Space
    x = 5
    nx = 100

    # create the time and spatial axis
    t_axis = np.linspace(0.0, t, nt + 1)
    x_axis = np.linspace(0.0, x, nx + 1)

    # Plot the Brownian Sheet
    ts, xs = np.meshgrid(t_axis, x_axis)

    fig = plt.figure(figsize=(8, 8))
    # plt.ion()
    plt.show(block=False)
    for i in range(50):
        # Compute the Brownian Sheet
        ax = fig.add_subplot(111, projection='3d')
        # ax = Axes3D(fig, auto_add_to_figure=False)
        fig.add_axes(ax)
        # ax.set_xlabel('$ 0 \\leq t \\leq {} $'.format(t), fontsize=14)
        # ax.set_ylabel('$0 \\leq x \\leq \\pi$', fontsize=14)
        ax.set_title('Brownian Sheet', fontsize=20)
        W_tx = BrownianSheet(t, nt, x, nx)
        ax.plot_surface(ts, xs, W_tx, rstride=1, cstride=1, cmap='plasma')
        plt.draw()
        plt.pause(0.1)
        plt.clf()
        # time.sleep(1)


def BM():
    # Set the time and space intervals. Choose number of partitions of each.
    # Time
    t = 100
    nt = 2000

    # create the time and spatial axis
    t_axis = np.linspace(0.0, t, nt + 1)
    plt.figure()
    # plt.ion()
    plt.show(block=False)
    for i in range(50):
        plt.title('Standard Brownian motion', fontsize=20)
        dW = np.random.normal(0, t / nt, size=nt)
        BM = np.zeros(nt+1)
        BM[1:nt+1] = np.cumsum(dW)
        plt.plot(t_axis, BM)
    plt.show()


if __name__ == "__main__":
    BrownianSheetMovie()
    # BM()
