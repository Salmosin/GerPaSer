import numpy as np

def TimeList(time_s,time_e,num_step):
    time = np.zeros(num_step)
    step = (time_e-time_s)/num_step
    for i in range(num_step):
        time[i] = time_s+i*step
    return [time,step]