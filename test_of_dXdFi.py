from input_data import *
import IndDiaG_exp as exp
import numpy as np
import matplotlib.pyplot as pl
import math
import GetHeatParts as HP

Cv = 26
Rm = 8.314
Hu = 42.5e6             #низшая теплота сгорания диз.топлива, Дж/кг
dxdfi = np.zeros((720,1))
dXdFiexp=np.zeros((720,1))
dXexp=np.zeros((720,1))
dxdfi_t1 = np.zeros((720,1))
dxdfi_t2 = np.zeros((720,1))
dxdfi_t = np.zeros((720,1))
p1 = np.zeros((720,1))
p2 = np.zeros((720,1))
Dif = np.zeros((720,1))
KiN = np.zeros((720,1))
qc = 7.02674088e-05         #цикловая подача топлива, кг
dfi = math.pi/180


def dXdfi():
    ExpData= exp.RdWte()
    Vc, Pc, Tc, Xc = ExpData

    for Fi in range(len(Pc) - 1):
       dXexp[Fi] =Xc[Fi+1]-Xc[Fi]
       if (dXexp[Fi] > 1) or (dXexp[Fi] < 0):
           dXexp[Fi] = 0
    pl.figure(1)
    pl.plot(dXexp)
    pl.grid(True)

    for Fi in range(len(Pc) - 1):
        dQ1 = Pc[Fi] * (Cv/Rm+1) * (Vc[Fi+1]-Vc[Fi])/dfi
        dQ2 = Cv/Rm*Vc[Fi]*(Pc[Fi+1]-Pc[Fi])/dfi
        dQ3 = HP.dQw( Pc[Fi],Tc[Fi],Fi)
        dXdFiexp[Fi] = (dQ1 + dQ2 + dQ3)*dfi/Hu/qc

    pl.plot(dXdFiexp)
    pl.grid(True)


def dXdfi_teor():
    ksi = 0.225
    dx = 0.99
    mt = 0.3
    mv = 1.75
    Fiz = 2
    Fic = 45
    C = -math.log(1 - dx)
    for fi in range(719-180):
        KiN[fi+180] = (mt / Fiz) * (fi / Fiz) ** mt * math.exp(-mt / (mt + 1) * (fi / Fiz) ** (mt + 1))
        Dif[fi+180] = C * ((mv + 1) / Fic) * (fi / Fic) ** mv * math.exp(-C * (fi / Fic) ** (mv + 1))
        dxdfi_t[fi+180] = (ksi * KiN[fi+180] + (1 - ksi) * Dif[fi+180])

    # pl.plot(ksi*KiN)
    #pl.plot((1 - ksi) *Dif)
    pl.plot(dxdfi_t)
    pl.grid(True)


dXdfi()
dXdfi_teor()
pl.xlim(179, 300)
pl.show()
if __name__ == '__main__':
    dXdfi_teor()