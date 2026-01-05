import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2

# построение всех точек по 2м координатам для всех моментов времени от одной точки в отсчетном положении
def TrajectoryByX1(x10, t, h):
    alltime = len(t)+1
    koord1= np.zeros(alltime)
    koord1[0] = x10
    for i in range(1,alltime):
        koord1[i] = RangeKutta(koord1[i-1],t[i],h,MotionLaw1)
    return koord1

def TrajectoryByX2(x20, t, h):
    alltime = len(t)+1
    koord2= np.zeros(alltime)
    koord2[0] = x20
    for i in range(1,alltime):
        koord2[i] = RangeKutta(koord2[i - 1], t[i], h, MotionLaw2)
    return koord2


