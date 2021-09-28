# importing the built-in module
import numpy as np
import matplotlib.pyplot as plt
# importing the user's module
from input_data import *
import IndDiaG_exp as exp
from GetWork import dL
from GetHeat import dQw
from Volume import Vol

# Постоянные расчета
N = 900  # количество расчетных шагов
Rm = 8.314  # универсальная газовая постоянная, Дж/моль/К
dFi = np.pi / 180  # приращение угла в радианах
Cv = 21  # теплоемкость, Дж/моль/К
# объявление массивов данных
V = np.zeros((N + 1, 1))  # объем КС, m^3
P = np.zeros((N + 1, 1))  # давление, Па
T = np.zeros((N + 1, 1))  # температура, K
M = np.zeros((N + 1, 1))  # кол-во вещества, моль


def main():
    # Чтение данныех экс. индикаторной диаграммы
    (Vexp, Texp, Pexp) = exp.RdWte()
    # Граничные условия на момент начала расчета
    P[Fi_zvk] = Pexp[Fi_zvk]
    T[Fi_zvk] = Texp[Fi_zvk]
    M[Fi_zvk] = P[Fi_zvk] * Vol(Fi_zvk) / T[Fi_zvk] / Rm
    Fi = Fi_zvk
    print(P[Fi_zvk], T[Fi_zvk], M[Fi_zvk], Vol(Fi_zvk))
    # Расчет процесса сжатия
    while Fi < 181:
        dT = (dL(P[Fi], Fi) + dQw(P[Fi], T[Fi], Fi)) / Cv / M[Fi]
        T[Fi + 1] = T[Fi] + dT * dFi
        M[Fi + 1] = M[Fi]
        P[Fi + 1] = M[Fi + 1] * T[Fi + 1] * Rm / Vol(Fi + 1)
        Fi += 1
    # Display temperature
    plt.figure(1)
    plt.plot(np.arange(0, N + 1), T, label="Trez")  # plotting the solved T
    plt.plot(np.arange(0, len(Texp)), Texp, label="Texp")  # plotting the exp T
    plt.title('Температура в КС')
    plt.ylabel('Температура, K')
    plt.xlabel('Угол поворота КВ, град')
    plt.grid(True)
    # Display temperature
    plt.figure(2)
    plt.plot(np.arange(0, N + 1), P, label="Prez")  # plotting the solved T
    plt.plot(np.arange(0, len(Pexp)), Pexp, label="Pexp")  # plotting the exp T
    plt.title('Давление в КС')
    plt.ylabel('Давление, Па')
    plt.xlabel('Угол поворота КВ, град')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()

# Меня смущает
# 1 - будет оцень много import
# 2 - как лучше сделать с графиками, а то строк и настроек много в основном коде - тупо функцию в которую передавать строки и массивы ?
#
