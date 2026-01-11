import math

import matplotlib.pyplot as plt
import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2

def risunok_taj(tekushi_x1, tekushi_x2, num_step):
        for i in range(num_step):
                plt.scatter(tekushi_x1[:, i], tekushi_x2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(tekushi_x1[:, 0], tekushi_x2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.scatter(tekushi_x1[:, num_step - 1], tekushi_x2[:, num_step - 1], s=10, c='blue', alpha=1, marker='o')
        plt.show()
def risunok_velo(tekushi_x1, tekushi_x2, time):
        len1 = len(tekushi_x1[0])
        len2 = len(tekushi_x1[1])
        velosity_vector_1 = np.zeros((len1, len2))
        velosity_vector_2 = np.zeros((len1, len2))
        for i in range(len1):
                for j in range(len2):
                        velosity_vector_1[i, j] = MotionLaw1(time[j], tekushi_x1[i, j])
                        velosity_vector_2[i, j] = MotionLaw2(time[j], tekushi_x2[i, j])
        for i in range(len2):
                plt.scatter(velosity_vector_1[:, i], velosity_vector_2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(velosity_vector_1[:, 0], velosity_vector_2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.scatter(velosity_vector_1[:, len2 - 1], velosity_vector_2[:, len2 - 1], s=10, c='blue', alpha=1, marker='o')
        print(velosity_vector_1[:, len2 - 1])
        print(velosity_vector_2[:, len2 - 1])

        plt.show()
def simple_streamlines(time):
    tekushi_x1 = np.linspace(0, 3, 20)
    tekushi_x2 = np.linspace(0, 3, 20)
    tekushi_X1, tekushi_X2 = np.meshgrid(tekushi_x1, tekushi_x2)
    V1 = -time * tekushi_X1                                                                #хз как эту скорость назвать
    V2 = -np.sin(time) * tekushi_X2                                                        #хз как эту скорость назвать
    plt.figure(figsize=(10, 8))
    plt.streamplot(tekushi_X1, tekushi_X2, V1, V2, color=np.sqrt(V1 ** 2 + V2 ** 2), cmap='viridis', linewidth=1, arrowsize=1.5, density=2)
    plt.grid(True, alpha=0.3)
    plt.show()
def risunok_trtr(koord_x1, koord_x2,time):
        for i in range(time):
                plt.scatter(koord_x1[:, i], koord_x2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(koord_x1[:, 0], koord_x2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.show()

def risunok_lines(koord_x1, koord_x2, time, shag, ID_Butcher):
            ang1 = np.zeros(len(koord_x1))
            ang2 = np.zeros(len(koord_x2))
            for i in range(len(koord_x1)):
                ang1[i] = RangeKutta(koord_x1[i], time, shag, MotionLaw1, ID_Butcher)
                ang2[i] = RangeKutta(koord_x2[i], time, shag, MotionLaw2, ID_Butcher)
            for i in range(len(koord_x2)):
                plt.plot([koord_x1[i], ang1[i]], [koord_x2[i], ang2[i]], 'b')
            plt.show()