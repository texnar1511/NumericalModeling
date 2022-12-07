from mlib import OptimizationMethods
import numpy as np
import math

def f(x):
    return abs(x-0.5)

print(OptimizationMethods.half_segment(function=f,a=0,b=1))

print(OptimizationMethods.golden_ration_naive(function=f,a=0,b=1))