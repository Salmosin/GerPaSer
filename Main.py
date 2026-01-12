from Butcher import get_num_butcher
from Class_Ring import Ring
from Plots import risunok_taj, risunok_velo, simple_streamlines, risunok_trtr, risunok_lines, simple_velo
from Time import TimeList
from Trajectory import TrajectoryByX
from Trajectory import TrajectoryByY
import numpy as np
start_koord_x10 = 230
start_koord_x20 = 125
butcher_num = 3
time_num = 80 #20 40 60 80 90
time_step = 100
ID_BUTCHER = get_num_butcher(butcher_num)
Rum = Ring(start_koord_x10,start_koord_x20, 4, 6)
all_ring = Rum.vivod_lista()
[time,shag] = TimeList(0,8,time_step)
time_local = time[time_num]
koord_X = np.zeros((len(all_ring[0]),time_step))
koord_Y = np.zeros((len(all_ring[1]),time_step))
for i in range(len(all_ring[0])):
    koord_1 = np.zeros(time_step)
    koord_2 = np.zeros(time_step)
    koord_1 = TrajectoryByX(all_ring[0,i],time,shag,ID_BUTCHER)
    koord_2 = TrajectoryByY(all_ring[1,i],time,shag,ID_BUTCHER)
    for j in range(time_step):
        koord_X[i, j] = koord_1[j]
        koord_Y[i, j] = koord_2[j]

risunok_taj(koord_X,koord_Y,time_step)#траектория полная

risunok_velo(koord_X,koord_Y,time)#скорось полная

risunok_lines(time_local, shag,time_num,get_num_butcher(5)) #линии тока самодельные
simple_streamlines(time_local) #линии тока функцией

risunok_trtr(koord_X,koord_Y,time_num) #положение в определенный момент времени + предыдущие
simple_velo(koord_X,koord_Y, time,time_num) #скорость в определенный момент времени + предыдущие