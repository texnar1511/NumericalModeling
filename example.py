from mlib import OptimizationMethods
from mlib import MathObjects
import numpy as np
import math

def f(x):
    return x[0]*x[1]+3*x[0]-2*x[1]

#print(OptimizationMethods.half_segment(function=f,a=0,b=1))

#print(OptimizationMethods.golden_ration_naive(function=f,a=0,b=1))

#print(MathObjects.first_derivate(function=f,point=[1,2],num_var=1))

m=MathObjects()

#print(f([3,2]))

#print(m.first_derivative_n_var(function=f,point=[3,1],num_var=0))

#print(m.gradient(function=f,point=[1,2]))

def g(x):
    return x**2+x

#print(m.first_derivative_1_var(g,7))

#print(m.add_num([1,2,3,4],0,5))

print(m.first_derivative_n_var(f,[1,2],0))

print(m.gradient(f,[1,2]))