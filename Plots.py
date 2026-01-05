import matplotlib.pyplot as plt
def risunok(x1, x2, t):
        for i in range(len(t)):
                plt.plot(x1[i], x2[i], 'r-')
        plt.show()
