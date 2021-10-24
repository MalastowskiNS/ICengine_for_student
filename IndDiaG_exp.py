import numpy as np

def RdWte():
    filename = "EngineSem.ind"
    datas = np.loadtxt(filename, skiprows=19)
    Pc = datas[:, 1]*100000    #давление, Па
    Tc = datas[:, 2]           #температура, К
    V = datas[:, 3]            #объем, м^3
    Xheat = datas[:, 8]        #доля сгоревшего топлива

    return V, Pc, Tc, Xheat


if __name__ == '__main__':
    RdWte()
