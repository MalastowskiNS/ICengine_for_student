# importing the built-in module
import numpy as np
import matplotlib.pyplot as pl
# importing the user's module
import IndDiaG_exp as exp
from input_data import Fi_ovik, Fi_zvik, Fi_ovk, Fi_zvk, n, Rm
from input_data import muf_int,  muf_exh
from input_data import Tk,  Pk, Tog, Pog

# заплатки
k = 1.3                               # показатель политропы
ml = 0.029                            # молярная масса
dFi = np.pi/180                       # приращение угла в радианах

def test():
    # Чтение данныех экс. индикаторной диаграммы
    ExpData = exp.RdWte()
    Vexp, Pexp, Texp, *rest = ExpData
    dGint = np.zeros((720, 1))
    dGexh = np.zeros((720, 1))
    for Fi in range(719):
        dGint[Fi] = getFlowRate(Pexp[Fi], Texp[Fi], Fi, 'int')/dFi     # потому, что для сравнения расход нужен в кг/с
        dGexh[Fi] = getFlowRate(Pexp[Fi], Texp[Fi], Fi, 'exh')/dFi     # потому, что для сравнения расход нужен в кг/с
    pl.plot(dGint)
    pl.plot(-dGexh)
    pl.grid(True)
    pl.show()



def getFlowRate (P, T, Fi, indx):
    (Tfar, Pfar, Pint, Tin, sign, psi) = (0, 0, 0, 0, 0, 0)
# Проверка канала
    if indx == 'exh':
        Tfar = Tog
        Pfar = Pog
    elif indx == 'int':
        Tfar = Tk
        Pfar = Pk
    else:
        print('Ошибка обозначения канала')
# Проверка входа/выхода
    if (P >= Pfar):
        Pint = P
        Tin = T
        Pout = Pfar
        sign = -1
    else:
        Pint = Pfar
        Tin = Tfar
        Pout = P
        sign = 1
# Пси
    if P > pow((k+1)/2, k/(k-1))*Pfar:
        psi = pow(2/(k+1), 1/(k-1))*(2*k/(k+1))**0.5
    else:
        dp = (Pout/Pint)
        psi = (2*k/(k-1)*(dp**(2/k)-dp**((k+1)/k)))**0.5
    dG = sign*muf_kl(Fi, indx)*psi*(Pint*Pint/Rm/Tin*ml)**0.5/(np.pi*n/30)
    return dG

def muf_kl(Fi, indx):
    (Fiok, Fizk, MuMax, muf) = (0, 0, 0, 0)
    todeg = np.pi / 180
    if indx == 'exh':
        Fiok = Fi_ovik
        Fizk = Fi_zvik
        MuMax = muf_exh
    elif indx == 'int':
        Fiok = Fi_ovk
        Fizk = Fi_zvk
        MuMax = muf_int
    else:
        print('Ошибка обозначения канала')

    if (Fiok <= Fi) and (Fi <= Fiok + 90):
        muf = MuMax * np.sin((Fi - Fiok)*todeg)
    elif (Fizk - 90 <= Fi) and (Fi <= Fizk):
        muf = MuMax * np.sin((Fi - Fizk + 180)*todeg)
    elif (Fizk - 90 + 720 <= Fi) and (Fi <= Fizk + 720):
        muf = MuMax * np.sin((Fi - Fizk + 180)*todeg)
    elif ((Fiok + 90 < Fi) and (Fi < Fizk - 90)) and (indx == 'exh'):
        muf = MuMax
    elif (Fiok + 90 < Fi) and (Fi < Fizk + 720 - 90) and (indx == 'int'):
        muf = MuMax
    else:
        muf = 0
    return muf

if __name__ == '__main__':
    test()