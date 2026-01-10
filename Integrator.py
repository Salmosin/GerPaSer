import numpy as np

from Butcher import get_butcher_tableau

def RangeKutta(x,t,h,func,Butcher):
    Tabl_B = get_butcher_tableau(Butcher)
    l = Tabl_B.length()
    f = np.zeros(l)
    A = Tabl_B.coeffsA()
    c = Tabl_B.coeffsC()
    b = Tabl_B.coeffsB()

    #Ранге-Кутт для системы с таблицой Бутчера извне
    for i in range(l):
        sum_f = 0
        for j in range(i):
            sum_f += A[i][j]*f[j]*h
        tk_i = t+c[i]*h
        xk_i = t+sum_f
        f[i] = func(tk_i,xk_i)
    delta_x = 0.0
    for i in range(l):
        delta_x += f[i]*h*b[i]
    return x+delta_x