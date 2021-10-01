# importing the built-in module
import numpy as np
import matplotlib.pyplot as plt
# importing the user's module
import GetHeatParts as lw
from input_data import *
import IndDiaG_exp as exp
from Volume import Vol
from Graph import graph

# Постоянные расчета
N=900                           # количество расчетных шагов
Rm=8.314                        # универсальная газовая постоянная, Дж/моль/К
dFi=np.pi/180                   # приращение угла в радианах
Cv=21                           # теплоемкость, Дж/моль/К
# объявление массивов данных
V=np.zeros((N+1,1))             # объем КС, m^3
P=np.zeros((N+1,1))             # давление, Па
T=np.zeros((N+1,1))             # температура, K
M=np.zeros((N+1,1))             # кол-во вещества, моль


def main():
 # Чтение данныех экс. индикаторной диаграммы
    (Vexp, Texp, Pexp) =exp.RdWte()
 # Граничные условия на момент начала расчета
    P[Fi_zvk] = Pexp[Fi_zvk]
    T[Fi_zvk] = Texp[Fi_zvk]
    M[Fi_zvk] = P[Fi_zvk] * Vol(Fi_zvk) / T[Fi_zvk] / Rm
    Fi=Fi_zvk
    print(P[Fi_zvk],T[Fi_zvk], M[Fi_zvk],Vol(Fi_zvk))
 # Расчет процесса сжатия
    while Fi < 181:
        dT=(lw.dL(P[Fi], Fi)+lw.dQw(P[Fi],T[Fi],Fi))/Cv/M[Fi]
        T[Fi+1]=T[Fi]+dT*dFi
        M[Fi+1]=M[Fi]
        P[Fi+1]=M[Fi+1]*T[Fi+1]*Rm/Vol(Fi+1)
        Fi += 1
 # Отображение результатов расчета
    plt.figure(1)
    graph(np.arange(0, len(Texp)), Texp, "Texp")
    graph(np.arange(0, N + 1), T, "Trez","Температура в КС", "Температура, K", "Угол поворота КВ, град")
    plt.figure(2)
    graph(np.arange(0, len(Pexp)), Pexp, "Pexp")
    graph(np.arange(0, N + 1), P, "Prez", "Давление в КС", "Давление, Па", "Угол поворота КВ, град")
    plt.show()



if __name__ == '__main__':
    main()



# Меня смущает
# 1 - будет оцень много import
# 2 - как лучше сделать с графиками, а то строк и настроек много в основном коде - тупо функцию в которую передавать строки и массивы ?
#from GetWork import dL
#from GetHeat import dQw

