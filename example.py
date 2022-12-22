from mlib import OptimizationMethods
import numpy as np
import math

def k(x):
    return x[0]**2+np.sin(x[1])

def f(x):
    return x[0]**2+x[1]**2

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

def k(x):
    return x[0]**2+np.sin(x[1])

def f(x):
    return x[0]**2+x[1]**2

def m(x):
    return x[0]+x[1]

print(o.gradient_method(k,[-1,-1],[2,2]))
print(o.projection_gradient_method(k,[-1,-1],[2,2]))


#print([0]*3)
#x=[1,2]
#print(eval('2*np.sin(x[0])+np.sinh(x[1])**2'))

#input=input()
#print(input)

# def a(x):
#     return eval(input)

#print(o.gradient_method(a,[-1,-1],[2,2]))
# x=[1,2]
# a=[1,3,13]

# print(a[:len(x)])
# print(a[len(x):])

# a=[1,2]

# b=[3,5]

# print(b+[0])

# print(b)

a=[-1,-1]
b=[2,2]

x0=[(i+j)/2 for i,j in zip(a,b)]
y0=np.sqrt(sum([(i-j)**2 for (i,j) in zip(a,b)]))/2
# print(x0)
# print(y0)

# def g_k(xa):
#     return sum([(x1-x_k+xa[len(x0):][0]*y)**2 for (x1,x_k,y) in zip(xa[:len(x0)],x0,o.gradient(f,x0))])

# print(g_k([0,0,1]))
# xa1=[0,0,1]
# print(xa1)
# print(x0)
# print(o.gradient(f,x0))
# print(xa1[:len(x0)])
# print(xa1[len(x0):][0])

#print(np.pi**2/4+np.pi/2+1/2)
#print(9/2)
