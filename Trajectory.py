import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2
# построение всех точек по 2м координатам для всех моментов времени от одной точки в отсчетном положении
def TrajectoryByX(start_koord_x10, time, shag,ID_Butcher):
    alltime = len(time)
    koord1= np.zeros(alltime)
    koord1[0] = start_koord_x10
    for i in range(1,alltime):
        koord1[i] = RangeKutta(koord1[i-1],time[i],shag,MotionLaw1, ID_Butcher)
    return koord1

def TrajectoryByY(start_koord_x20, time, shag,ID_Butcher):
    alltime = len(time)
    koord2= np.zeros(alltime)
    koord2[0] = start_koord_x20
    for i in range(1,alltime):
        koord2[i] = RangeKutta(koord2[i - 1], time[i], shag, MotionLaw2, ID_Butcher)
    return koord2

