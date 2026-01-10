import matplotlib.pyplot as plt

from Butcher import get_num_butcher
from Class_Ring import Ring
from Plots import risunok_taj, risunok_velo, simple_streamlines, risunok_trtr, risunok_lines
from Time import TimeList
from Trajectory import TrajectoryByX
from Trajectory import TrajectoryByY
import numpy as np
x10 = 230
x20 = 125
but_num = 3
time_num = 20
time_step = 100
ID_BUTCHER = get_num_butcher(but_num)
Rum = Ring(x10,x20, 4, 6)
all_ring = Rum.vivod_lista()
[t,h] = TimeList(0,8,time_step)
t_local = t[time_num]
koord_X = np.zeros((len(all_ring[0]),time_step))
koord_Y = np.zeros((len(all_ring[1]),time_step))
for i in range(len(all_ring[0])):
    koord_1 = np.zeros(time_step)
    koord_2 = np.zeros(time_step)
    koord_1 = TrajectoryByX(all_ring[0,i],t,h,ID_BUTCHER)
    koord_2 = TrajectoryByY(all_ring[1,i],t,h,ID_BUTCHER)
    for j in range(time_step):
        koord_X[i, j] = koord_1[j]
        koord_Y[i, j] = koord_2[j]

#risunok(koord_X,koord_Y,time_step)

#risunok_velo(koord_X,koord_Y,t)
risunok_lines(koord_X[:,time_num],koord_Y[:,time_num],t_local,h,get_num_butcher(5))
#simple_streamlines(t_local)
#risunok_trtr(koord_X,koord_Y,time_num)
