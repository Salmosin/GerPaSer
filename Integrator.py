import numpy as np

from Butcher import get_butcher_tableau

def RangeKutta(x,time,shag,func,ID_Butcher):
    Tabl_B = get_butcher_tableau(ID_Butcher)
    num_stages_l = Tabl_B.length()
    f = np.zeros(num_stages_l)
    matrix_A = Tabl_B.coeffsA()
    time_steps_c = Tabl_B.coeffsC()
    weights_b = Tabl_B.coeffsB()

    #Ранге-Кутт для системы с таблицой Бутчера извне
    for i in range(num_stages_l):
        sum_f = 0
        for j in range(i):
            sum_f += matrix_A[i][j]*f[j]*shag
        time_k_i = time+time_steps_c[i]*shag
        xk_i = time+sum_f
        f[i] = func(time_k_i,xk_i)
    delta_x = 0.0
    for i in range(num_stages_l):
        delta_x += f[i]*shag*weights_b[i]
    return x+delta_x