# importing the built-in module
import numpy as np
# importing the user's module
from Volume import Vol
from input_data import D, S, eps, n


def dQw(P, T, Fi):
    delta = 0.005
    T_h = 250
    T_cyl = 180
    T_p = 275
    Cm = S * n / 30
    Fpist = np.pi * D ** 2 / 4
    Vh = Fpist * S
    Vc = Vh / (eps - 1)
    Fcyl = ((Vol(Fi) - Vc) / Fpist + delta) * np.pi * D
    alfa_w = 77.9 * 10 ** (-4) * Cm ** (1 / 3) * np.sqrt(P * T)
    dQh = alfa_w * (T - T_h) * 1.4 * Fpist
    dQcyl = alfa_w * (T - T_cyl) * Fcyl
    dQp = alfa_w * (T - T_p) * Fpist
    dq = -(dQp + dQcyl + dQh) / (np.pi * n / 30)
    return dq
