import numpy as np

def TimeList(time_s,time_e,num_step):
    t = np.zeros(num_step)
    step = (time_e-time_s)/num_step
    for i in range(num_step):
        t[i] = time_s+i*step
    return [t,step]