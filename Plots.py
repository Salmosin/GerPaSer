import matplotlib.pyplot as plt
import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2

def risunok(x1, x2, t):
        for i in range(len(t)):
                plt.plot(x1[i], x2[i], 'r-')
        plt.show()
def risunok_velo(x1,x2,t):
        v1 = np.zeros(len(t))
        v2 = np.zeros(len(t))
        for i in range(len(t)):
                v1[i] = MotionLaw1(t[i],x1[i])
                v2[i] = MotionLaw2(t[i],x2[i])
        for i in range(len(t)):
                plt.plot(v1[i], v2[i], 'b-')
        plt.show()

