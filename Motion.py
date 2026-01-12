import math

# законы движения для 2х координат
def MotionLaw1(time,koord_x):
    velo1 = -time * koord_x
    return velo1

def MotionLaw2(time,koord_x):
    velo2 = -math.sin(time)*koord_x
    return velo2

