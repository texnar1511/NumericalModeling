from mlib import OptimizationMethods
import numpy as np
import math

# def f(x):
#     return x[0]*x[1]+3*x[0]*x[2]-2*x[1]+np.sin(x[2])

def f(x):
    return x[0]**2+np.sin(x[1])

#print(OptimizationMethods.half_segment(function=f,a=0,b=1))

#print(OptimizationMethods.golden_ration_naive(function=f,a=0,b=1))

#print(MathObjects.first_derivate(function=f,point=[1,2],num_var=1))

o=OptimizationMethods()

#print(f([3,2]))

#print(m.first_derivative_n_var(function=f,point=[3,1],num_var=0))

#print(m.gradient(function=f,point=[1,2]))

def g(x):
    return 3

#print(m.first_derivative_1_var(g,7))

#print(m.add_num([1,2,3,4],0,5))

#print(o.first_derivative_n_var(f,[1,2],0))

#print(o.gradient(f,[1,2]))

#print([(x+y)/2 for x,y in zip([1,2,3],[2,3,5])])

#print(o.half_segment(g,1,2))
#print(o.golden_ration_naive(g,1,2))
print(o.gradient_method(f,[-1,-1],[2,2]))

#print([0]*3)