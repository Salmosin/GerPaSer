import math

import matplotlib.pyplot as plt
import numpy as np

from Integrator import RangeKutta
from Motion import MotionLaw1
from Motion import MotionLaw2

def risunok_taj(x1, x2,num_step):
        for i in range(num_step):
                plt.scatter(x1[:, i], x2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(x1[:, 0], x2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.scatter(x1[:, num_step-1], x2[:, num_step-1], s=10, c='blue', alpha=1, marker='o')
        plt.show()
def risunok_velo(x1, x2, t):
        len1 = len(x1[0])
        len2 = len(x1[1])
        v1 = np.zeros((len1,len2))
        v2 = np.zeros((len1,len2))
        for i in range(len1):
                for j in range(len2):
                        v1[i, j] = MotionLaw1(t[j], x1[i, j])
                        v2[i, j] = MotionLaw2(t[j], x2[i, j])
        for i in range(len2):
                plt.scatter(v1[:, i], v2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(v1[:, 0], v2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.scatter(v1[:, len2-1], v2[:, len2-1], s=10, c='blue', alpha=1, marker='o')
        print(v1[:, len2-1])
        print(v2[:, len2-1])

        plt.show()
def simple_streamlines(t):
    x1 = np.linspace(0, 3, 20)
    x2 = np.linspace(0, 3, 20)
    X1, X2 = np.meshgrid(x1, x2)
    V1 = -t * X1
    V2 = -np.sin(t) * X2
    plt.figure(figsize=(10, 8))
    plt.streamplot(X1, X2, V1, V2,color=np.sqrt(V1**2 + V2**2), cmap='viridis',linewidth=1,arrowsize=1.5,density=2)
    plt.grid(True, alpha=0.3)
    plt.show()
def risunok_trtr(x1, x2,t):
        for i in range(t):
                plt.scatter(x1[:, i], x2[:, i], s=10, c='green', alpha=1, marker='o')
        plt.scatter(x1[:, 0], x2[:, 0], s=10, c='red', alpha=1, marker='o')
        plt.show()

def risunok_lines(x1, x2, t, h, ID_Butcher):
            ang1 = np.zeros(len(x1))
            ang2 = np.zeros(len(x2))
            for i in range(len(x1)):
                ang1[i] = RangeKutta(x1[i], t, h, MotionLaw1, ID_Butcher)
                ang2[i] = RangeKutta(x2[i], t, h, MotionLaw2, ID_Butcher)
            for i in range(len(x2)):
                plt.plot([x1[i], ang1[i]], [x2[i], ang2[i]], 'b')
            plt.show()