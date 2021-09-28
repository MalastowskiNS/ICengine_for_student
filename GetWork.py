# importing the built-in module
import numpy as np
# importing the user's module
from Volume import Vol

dFi = np.pi / 180  # приращение угла в радианах


def dL(P, Fi):
    dl = -P * (Vol(Fi + 1) - Vol(Fi)) / dFi
    return dl
