import matplotlib.pyplot as plt


def graph(X, Y, lab=None, tit=None, ylab=None, xlab=None):

    #plt.plot(data[:][0], data[:][1],  label=lab)
    plt.plot(X, Y, label=lab)
    plt.title(tit)
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.grid(True)
