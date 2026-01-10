import math

# законы движения для 2х координат
def MotionLaw1(t,x):
    velo1 = -t * x
    return velo1

def MotionLaw2(t,x):
    velo2 = -math.sin(t)*x
    return velo2

