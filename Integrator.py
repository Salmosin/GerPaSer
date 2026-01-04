import matplotlib.pyplot as plt
import numpy as np
from Butcher
def RangeKutta(x,t,h,func):
    l = Butcher.length()
    f = np.zeros(l)
    A = Butcher.coeffsA()
    c = Butcher.coeffsC()
    b = Butcher.coeffsB()
    for i in range(l):
        sum_f = 0
        for j in range(i):
            sum_f += A[i][j]*f[i]*h
        tk_i = t+c[i]*h
        xk_i = t+sum_f
        f[i] = func(tk_i,xk_i)
    delta_x = 0
    for i in range(l):
        delta_x += f[i]*h*b[i]
    return x+delta_x