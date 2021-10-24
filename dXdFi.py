# importing the built-in module
import math
# importing the user's module
from input_data import *


def dXdfi(fi):
    fi = fi-180+Fi_ovt
    ksi = 0.225
    dx = 0.99
    mt = 0.3
    mv = 1.75
    Fiz = 2
    Fic = 45
    C = -math.log(1 - dx)
    if (fi<180) and (fi>0):
        KiN = (mt / Fiz) * (fi / Fiz) ** mt * math.exp(-mt / (mt + 1) * (fi / Fiz) ** (mt + 1))
        Dif = C * ((mv + 1) / Fic) * (fi / Fic) ** mv * math.exp(-C * (fi / Fic) ** (mv + 1))
        dx = ksi * KiN + (1 - ksi) * Dif
    else:
        dx = 0
    return dx
if __name__ == '__main__':
    dXdfi(0)