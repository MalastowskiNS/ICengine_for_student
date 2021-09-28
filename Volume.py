# importing the built-in module
import numpy as np
# importing the user's module
from input_data import D, S, eps, lamb


def Vol(deg):
    deg = deg * np.pi / 180
    Ap = np.pi * D ** 2 / 4
    Vh = Ap * S
    Vc = Vh / (eps - 1)
    rez = Vc + Vh - Ap * S / 2 * (1 - np.cos(deg) - lamb / 4 * (1 - np.cos(2 * deg)))
    return (rez)
