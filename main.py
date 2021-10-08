# importing the built-in module
import numpy as np
import matplotlib.pyplot as plt
# importing the user's module
import GetHeatParts as lw
import get_properties as gp
from input_data import *
import IndDiaG_exp as exp
from Volume import Vol
from Graph import graph

# Постоянные расчета
N=900                           # количество расчетных шагов
Rm=8.314                        # универсальная газовая постоянная, Дж/моль/К
dFi=np.pi/180                   # приращение угла в радианах
# объявление массивов данных
V=np.zeros((N+1,1))             # объем КС, m^3
P=np.zeros((N+1,1))             # давление, Па
T=np.zeros((N+1,1))             # температура, K
# кол-во вещества, моль
M = {
    'N2':  np.zeros((N+1,1)),
    'O2':  np.zeros((N+1,1)),
    'CO2': np.zeros((N+1,1)),
    'H2O': np.zeros((N+1,1)),
    'Mixture': np.zeros((N+1,1))
}

def main():
 # Чтение данныех экс. индикаторной диаграммы
    (Vexp, Texp, Pexp) =exp.RdWte()
 # Граничные условия на момент начала расчета
    P[Fi_zvk] = Pexp[Fi_zvk]
    T[Fi_zvk] = Texp[Fi_zvk]
    M['Mixture'][Fi_zvk]=P[Fi_zvk] * Vol(Fi_zvk) / T[Fi_zvk] / Rm
    M['N2'][Fi_zvk] = 0.79 * M['Mixture'][Fi_zvk]
    M['O2'][Fi_zvk] = 0.21 * M['Mixture'][Fi_zvk]
    M['CO2'][Fi_zvk] = 0
    M['H2O'][Fi_zvk] = 0
    Fi=Fi_zvk
    print(P[Fi_zvk],T[Fi_zvk], M['Mixture'][Fi_zvk],Vol(Fi_zvk))
 # Расчет процесса сжатия
    while Fi < 181:
        Cv=gp.get_properties({key:value[Fi] for (key,value) in M.items()},T[Fi])
        dT=(lw.dL(P[Fi], Fi)+lw.dQw(P[Fi],T[Fi],Fi))/Cv/M['Mixture'][Fi]
        T[Fi+1]=T[Fi]+dT*dFi
        M['N2'][Fi+1] =  M['N2'][Fi]
        M['O2'][Fi+1] =  M['O2'][Fi]
        M['CO2'][Fi+1] = M['CO2'][Fi]
        M['H2O'][Fi+1] = M['H2O'][Fi]
        M['Mixture'][Fi+1] =M['N2'][Fi+1]+M['O2'][Fi+1]+M['CO2'][Fi+1]+M['H2O'][Fi+1]
        P[Fi+1]=M['Mixture'][Fi+1]*T[Fi+1]*Rm/Vol(Fi+1)
        Fi += 1
 # Отображение результатов расчета
    plt.figure(1)
    graph(np.arange(0, len(Texp)), Texp, "Texp")
    graph(np.arange(0, N + 1), T, "Trez","Температура в КС", "Температура, K", "Угол поворота КВ, град")
    plt.figure(2)
    graph(np.arange(0, len(Pexp)), Pexp, "Pexp")
    graph(np.arange(0, N + 1), P, "Prez", "Давление в КС", "Давление, Па", "Угол поворота КВ, град")
    plt.show()
    plt.figure(3)
    graph(np.arange(0, N + 1), M['Mixture'], "Кол-во вещества", "Вещества в цилиндре", "Mixture, моль", "Угол поворота КВ, град")
    plt.show()



if __name__ == '__main__':
    main()

