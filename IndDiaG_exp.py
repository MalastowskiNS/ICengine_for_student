import numpy as np
import matplotlib.pyplot as plt


def RdWte():
    filename = "EngineSem.ind"
    datas = np.loadtxt(filename, skiprows=19)
    Fi = datas[:, 0]
    Press = datas[:, 1] * 10 ** 5
    T = datas[:, 2]
    V = datas[:, 3]
    # plt.plot(Fi, Press)  # plotting the points
    # plt.grid(True)
    # plt.show()  # Display the plot
    return V, T, Press


if __name__ == '__main__':
    RdWte()
