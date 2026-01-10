import cmath

import matplotlib.pyplot as plt
import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2

def risunok(x1, x2,kolvo_points,num_step):
        for i in range(num_step):
                for j in range(kolvo_points):
                        plt.plot(x1[j,i], x2[j,i], 'r')
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
def risunok_lines(x1,x2,t,x0,h):
        v1 = np.zeros(len(t))
        v2 = np.zeros(len(t))
        sl1 = np.zeros(len(t))
        sl2 = np.zeros(len(t))
        for i in range(len(t)):
                v1[i] = MotionLaw1(t,x1[i])
                v2[i] = MotionLaw2(t,x2[i])
                ang = RangeKutta(x0,t,h,MotionLaw1,)
                sl1[i] = v1[i] + 1 / cmath.sqrt(1 + ang ** 2)
                sl2[i] = v2[i] + ang / cmath.sqrt(1 + ang ** 2)
        for i in range(len(t)):
                plt.plot([v1[i], sl1[i]], [v2[i], sl2[i]], 'b-')
                plt.plot(v1[i], v2[i], 'ro', )
        plt.show()

