import math
import numpy
from matplotlib import pyplot


# define the function for the velocity vortex
def get_velocity_vortex(strength, xv, yv, X, Y):
    u = strength / (2 * numpy.pi) * (Y - yv) / ((X - xv)**2 + (Y - yv)**2)
    v = -strength / (2 * numpy.pi) * (X - xv) / ((X - xv)**2 + (Y - yv)**2)
    return u,v
    
# define the stream function for the vortex
def get_stream_function_vortex(strength, xv, yv, X, Y):
    psi = strength / (4 * math.pi) * numpy.log((X - xv)**2 + (Y - yv)**2)
    return psi


# define a the function for the sink velocity
def get_velocity_sink(strength, xs, ys, X, Y):
    u = strength / (2 * numpy.pi) * (X - xs) / ((X - xs)**2 + (Y - ys)**2)
    v = strength / (2 * numpy.pi) * (Y - ys) / ((X - xs)**2 + (Y - ys)**2)
    return u, v
    
def get_stream_function_sink(strength, xs, ys, X, Y):
    psi = strength / (2 * numpy.pi) * numpy.arctan2((Y - ys), (X - xs))
    return psi
    

