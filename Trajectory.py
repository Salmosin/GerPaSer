import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2
# построение всех точек по 2м координатам для всех моментов времени от одной точки в отсчетном положении
def TrajectoryByX(x10, t, h,ID_Butcher):
    alltime = len(t)
    koord1= np.zeros(alltime)
    koord1[0] = x10
    for i in range(1,alltime):
        koord1[i] = RangeKutta(koord1[i-1],t[i],h,MotionLaw1, ID_Butcher)
    return koord1

def TrajectoryByY(x20, t, h,ID_Butcher):
    alltime = len(t)
    koord2= np.zeros(alltime)
    koord2[0] = x20
    for i in range(1,alltime):
        koord2[i] = RangeKutta(koord2[i - 1], t[i], h, MotionLaw2, ID_Butcher)
    return koord2

