from mlib import OptimizationMethods
import numpy as np
import math

def f(x):
    return math.sin(x)

print(OptimizationMethods.half_segment(function=f,a=0,b=10))

print(OptimizationMethods.golden_ration_naive(function=f,a=0,b=10))