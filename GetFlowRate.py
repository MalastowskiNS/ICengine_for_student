# importing the built-in module
import numpy as np
import matplotlib.pyplot as pl
# importing the user's module
import IndDiaG_exp as exp
from input_data import Fi_ovik, Fi_zvik, Fi_ovk, Fi_zvk, n, Rm
from input_data import muf_int,  muf_exh
from input_data import Tk,  Pk, Tog, Pog
from const import ml_sp
import get_properties as gp

# заплатки
k = 1.3                               # показатель политропы
dFi = np.pi/180                       # приращение угла в радианах
#Mles = {'N2':  0.0652828008625491,
#        'O2':  0.0173536559254877,
#        'CO2': 0,
#       'H2O': 0,
#        'Mixture': 0.0826364567880368
#        }
# Мольные доли веществ
# Газ на входе (воздух)
rin = {
    'N2': 0.79,
    'O2': 0.21,
    'CO2': 0,
    'H2O': 0,
    'Mixture': 1
     }
ml_in = rin['N2']*ml_sp['N2']+rin['O2']*ml_sp['O2']+rin['CO2']*ml_sp['CO2']+rin['H2O']*ml_sp['H2O']
# Газ на выходе (чистый ОГ)
rout = {
    'N2': 0.7212,
    'O2': 0.0959,
    'CO2': 0.0668,
    'H2O': 0.1161,
    'Mixture': 1
        }
ml_out = rout['N2']*ml_sp['N2']+rout['O2']*ml_sp['O2']+rout['CO2']*ml_sp['CO2']+rout['H2O']*ml_sp['H2O']


def getFlowRate(P, T, Moles, Fi, indx):
    (Tfar, Pfar, Pint, Tin, sign, psi, mlfar, rfar, ml, r) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    dM0 = {
        'N2': 0,
        'O2': 0,
        'CO2': 0,
        'H2O': 0,
        'Mixture': 0
    }
# Определение долей веществ в КС
    r0 = {
        'N2': Moles['N2']/Moles['Mixture'],
        'O2': Moles['O2']/Moles['Mixture'],
        'CO2': Moles['CO2']/Moles['Mixture'],
        'H2O': Moles['H2O']/Moles['Mixture'],
        'Mixture': 1
    }
    ml0 = r0['N2'] * ml_sp['N2'] + r0['O2'] * ml_sp['O2'] + r0['CO2'] * ml_sp['CO2'] + r0['H2O'] * ml_sp['H2O']
# Проверка канала
    if indx == 'exh':
        Tfar = Tog
        Pfar = Pog
        mlfar = ml_out
        rfar = rout
    elif indx == 'int':
        Tfar = Tk
        Pfar = Pk
        mlfar = ml_in
        rfar = rin
    else:
        print('Ошибка обозначения канала')
# Проверка входа/выхода
    if P >= Pfar:
        Pint = P
        Tin = T
        Pout = Pfar
        sign = -1
        r = r0
        ml = ml0
    else:
        Pint = Pfar
        Tin = Tfar
        Pout = P
        sign = 1
        r = rfar
        ml = mlfar
# Пси
    if P > pow((k+1)/2, k/(k-1))*Pfar:
        psi = pow(2/(k+1), 1/(k-1))*(2*k/(k+1))**0.5
    else:
        dp = (Pout/Pint)
        psi = (2*k/(k-1)*(dp**(2/k)-dp**((k+1)/k)))**0.5

    dG = sign*muf_kl(Fi, indx)*psi*(Pint*Pint/Rm/Tin*ml)**0.5/(np.pi*n/30)
    dM0['Mixture'] = 1 / ml * dG
    dM0['N2'] = r['N2'] * dM0['Mixture']
    dM0['O2'] = r['O2'] * dM0['Mixture']
    dM0['CO2'] = r['CO2'] * dM0['Mixture']
    dM0['H2O'] = r['H2O'] * dM0['Mixture']
    cp = gp.get_properties(r, Tin) + Rm
    dH = cp * Tin * dM0['Mixture']

    return dM0, dH


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


def test():
    # Чтение данныех экс. индикаторной диаграммы
    ExpData = exp.RdWte()
    Vexp, Pexp, Texp, *rest = ExpData
    dGint = np.zeros((720, 1))
    dGexh = np.zeros((720, 1))
    intake = np.zeros((720, 1))
    exhaust = np.zeros((720, 1))
    Fi=680
    print(Pexp[Fi])
    [dMin, dHin]=getFlowRate(Pexp[Fi], Texp[Fi], Mles, Fi, 'int')
    [dMout, dHout] = getFlowRate(Pexp[Fi], Texp[Fi], Mles, Fi, 'exh')
    print(dHin)
    print(dHout)
 #   for Fi in range(719):
    #    dGint[Fi] = getFlowRate(Pexp[Fi], Texp[Fi], Mles, Fi, 'int')/dFi     # потому, что для сравнения расход нужен в кг/с
    #    dGexh[Fi] = getFlowRate(Pexp[Fi], Texp[Fi], Mles, Fi, 'exh')/dFi     # потому, что для сравнения расход нужен в кг/с
    #    intake[Fi] = muf_kl(Fi, 'int')
    #    exhaust[Fi] = muf_kl(Fi, 'exh')

    #pl.figure(1)
    #pl.plot(dGint)
    #pl.plot(dGexh)
    #pl.grid(True)

    #pl.figure(2)
    #pl.plot(intake)
    #pl.plot(exhaust)
    #pl.grid(True)
    #pl.show()


if __name__ == '__main__':
    test()
