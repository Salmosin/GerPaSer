def TimeList(time_s,time_e,num_step):
    t = []
    step = (time_e-time_s)/num_step
    for i in range(num_step):
        t.append(time_s+i*step)
    return t