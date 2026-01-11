import matplotlib.pyplot as plt
import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2

def risunok_taj(history_x1, history_x2,num_step):
        for i in range(num_step):
                plt.scatter(history_x1[:, i], history_x2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(history_x1[:, 0], history_x2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.scatter(history_x1[:, num_step-1], history_x2[:, num_step-1], s=10, c='blue', alpha=1, marker='o')
        plt.show()
def risunok_velo(history_x1, history_x2, time):
        len1 = len(history_x1[0])
        len2 = len(history_x1[1])
        velosity_1 = np.zeros((len1,len2))
        velosity_2 = np.zeros((len1,len2))
        for i in range(len1):
                for j in range(len2):
                        velosity_1[i, j] = MotionLaw1(time[j], history_x1[i, j])
                        velosity_2[i, j] = MotionLaw2(time[j], history_x2[i, j])
        for i in range(len2):
                plt.scatter(velosity_1[:, i], velosity_2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(velosity_1[:, 0], velosity_2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.scatter(velosity_1[:, len2-1], velosity_2[:, len2-1], s=10, c='blue', alpha=1, marker='o')
        print(velosity_1[:, len2-1])
        print(velosity_2[:, len2-1])

        plt.show()
def simple_streamlines(time):
    koord_x1 = np.linspace(0, 240, 50)
    koord_x2 = np.linspace(0, 140, 50)
    koord_X1, koord_X2 = np.meshgrid(koord_x1, koord_x2)
    Velosity_1 = -time * koord_X1
    Velosity_2 = -np.sin(time) * koord_X2
    plt.figure(figsize=(10, 8))
    plt.streamplot(koord_X1, koord_X2, Velosity_1, Velosity_2,color=np.sqrt(Velosity_1**2 + Velosity_2**2), cmap='viridis',linewidth=1,arrowsize=1.5,density=2)
    plt.grid(True, alpha=0.3)
    plt.show()
def simple_velo(koord_x1, koord_x2,time,time_local):
    len1 = len(koord_x1[0])
    velosity_1 = np.zeros((len1, time_local))
    velosity_2 = np.zeros((len1, time_local))
    for i in range(len1):
        for j in range(time_local):
            velosity_1[i, j] = MotionLaw1(time[j], koord_x1[i, j])
            velosity_2[i, j] = MotionLaw2(time[j], koord_x2[i, j])
    for i in range(time_local):
            plt.scatter(velosity_1[:, i], velosity_2[:, i], s=10, c='green', alpha=1, marker='o')
    plt.scatter(velosity_1[:, 0], velosity_2[:, 0], s=10, c='red', alpha=1, marker='o')
    plt.show()

def risunok_trtr(koord_x1, koord_x2, time):
    for i in range(time):
        plt.scatter(koord_x1[:, i], koord_x2[:, i], s=10, c='green', alpha=1, marker='o')
    plt.scatter(koord_x1[:, 0], koord_x2[:, 0], s=10, c='red', alpha=1, marker='o')
    plt.show()

def risunok_lines(time, shag, time_l, ID_Butcher):
    koord_x1 = np.linspace(50, 250, 50)
    koord_x2 = np.linspace(140, 0, 50)

    ang1 = np.zeros(len(koord_x1))
    ang2 = np.zeros(len(koord_x1))
    koord_x11 = np.zeros(len(koord_x1))
    koord_x22 = np.zeros(len(koord_x1))
    for i in range(len(koord_x1)):
        ang1[i] = RangeKutta(koord_x1[i], time, shag, MotionLaw1, ID_Butcher)
        ang2[i] = RangeKutta(koord_x2[i], time, shag, MotionLaw2, ID_Butcher)
        koord_x11[i] = koord_x1[i] + (ang1[i] - koord_x1[i]) * (100-time_l)
        koord_x22[i] = koord_x2[i] + (ang2[i] - koord_x2[i]) * (100-time_l)
    for i in range(len(koord_x2)):
        plt.plot([koord_x1[i], koord_x11[i]], [koord_x2[i], koord_x22[i]], 'b')
    plt.show()