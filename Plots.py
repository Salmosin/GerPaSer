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
        plt.show()
def simple_streamlines(t):
    x1 = np.linspace(0, 240, 50)
    x2 = np.linspace(0, 140, 50)
    koord_X1, koord_X2 = np.meshgrid(x1, x2)
    Velosity_1 = -t * koord_X1
    Velosity_2 = -np.sin(t) * koord_X2
    plt.figure(figsize=(10, 8))
    plt.streamplot(koord_X1, koord_X2, Velosity_1, Velosity_2,color=np.sqrt(Velosity_1**2 + Velosity_2**2), cmap='viridis',linewidth=1,arrowsize=1.5,density=2)
    plt.grid(True, alpha=0.3)
    plt.show()
def simple_velo(x1, x2,t,t_local):
    len1 = len(x1[0])
    v1 = np.zeros((len1, t_local))
    v2 = np.zeros((len1, t_local))
    for i in range(len1):
        for j in range(t_local):
            v1[i, j] = MotionLaw1(t[j], x1[i, j])
            v2[i, j] = MotionLaw2(t[j], x2[i, j])
    for i in range(t_local):
            plt.scatter(v1[:, i], v2[:, i], s=10, c='green', alpha=1, marker='o')
    plt.scatter(v1[:, 0], v2[:, 0], s=10, c='red', alpha=1, marker='o')
    plt.scatter(v1[:, t_local-1], v2[:, t_local-1], s=10, c='blue', alpha=1, marker='o')
    plt.show()

def risunok_trtr(x1, x2, t):
    for i in range(t):
        plt.scatter(x1[:, i], x2[:, i], s=10, c='green', alpha=1, marker='o')
    plt.scatter(x1[:, 0], x2[:, 0], s=10, c='red', alpha=1, marker='o')
    plt.scatter(x1[:, t], x2[:, t], s=10, c='blue', alpha=1, marker='o')
    plt.show()

def risunok_lines(t, h, t_l, ID_Butcher):
    x1 = np.linspace(50, 250, 50)
    x2 = np.linspace(140, 0, 50)

    ang1 = np.zeros(len(x1))
    ang2 = np.zeros(len(x1))
    x11 = np.zeros(len(x1))
    x22 = np.zeros(len(x1))
    for i in range(len(x1)):
        ang1[i] = RangeKutta(x1[i], t, h, MotionLaw1, ID_Butcher)
        ang2[i] = RangeKutta(x2[i], t, h, MotionLaw2, ID_Butcher)
        x11[i] = x1[i] + (ang1[i] - x1[i]) * (100-t_l)
        x22[i] = x2[i] + (ang2[i] - x2[i]) * (100-t_l)
    for i in range(len(x2)):
        plt.plot([x1[i], x11[i]], [x2[i], x22[i]], 'b')
    plt.show()