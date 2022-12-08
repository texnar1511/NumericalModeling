from mlib import OptimizationMethods
from mlib import MathObjects
import numpy as np
import math

def f(x):
    return x*x

def f(x1,x2):
    return x1+x2

#print(OptimizationMethods.half_segment(function=f,a=0,b=1))

#print(OptimizationMethods.golden_ration_naive(function=f,a=0,b=1))

print(MathObjects.first_derivate(function=f,point=1))