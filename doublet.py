import math 
import numpy
from matplotlib import pyplot




def get_velocity_doublet(strength, xd, yd, X, Y):
    u = (-strength / (2* math.pi) * 
        ((X - xd)**2 - (Y - yd)**2) /
        ((X - xd)**2 + (Y - yd)**2)**2)
    v = (-strength / (2 * math.pi) * 
        2 * (X - xd) * (Y - yd) /
         ((X - xd)**2 + (Y-yd)**2)**2)
    return u, v
    
def get_stream_function_doublet(strength, xd, yd, X, Y):
    psi = - strength / (2* math.pi) * (Y - yd) / ((X - xd)**2 + (Y - yd)**2)
    
    return psi
    
