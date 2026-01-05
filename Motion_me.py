from sys import set_int_max_str_digits
import cmath
import numpy as np
from Integrator import RangeKutta

def Motion1(x0,t,h):
    func1 = -t
    alltime  = len(t)
    x1 = np.zeros(alltime)
    x1[1] = RangeKutta(x0, 0, h, func1)
    for i in range(2,alltime):
        x1[i] = RangeKutta(x1[i-1], t[i-1], h, func1)
    return x1

def Motion2(y0,t,h):
    func2 = -cmath.sin(t)
    alltime = len(t)
    x2 = np.zeros(alltime)
    x2[1] = RangeKutta(y0, 0, h, func2)
    for i in range(alltime):
        x2[i] = RangeKutta(x2[i-1], t[i-1], h, func2)
    return x2