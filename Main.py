from Class_Ring import Ring
from Plots import risunok
from Time import TimeList
from Trajectory import TrajectoryByX1
from Trajectory import TrajectoryByX2
import numpy as np
x10 = 230
x20 = 125

Rum = Ring(x10,x20, 4, 6)
all_ring = Rum.vivod_lista()
h = 0.01
t = TimeList(0,5,100)
koord1 = np.zeros(len(all_ring))
koord2 = np.zeros(len(all_ring))
for i in range(len(all_ring)):
    #Изменить в зависимости от интерпретации координат точки
    koord1[i] = TrajectoryByX1(all_ring[i].x,t,h)
    koord2[i] = TrajectoryByX2(all_ring[i].y,t,h)
risunok(koord1,koord2)


