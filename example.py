from mlib import OptimizationMethods
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

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

#print(o.gradient_method(k,[-1,-1],[2,2]))
#print(o.projection_gradient_method(m,[-1,-1],[2,2],'cube'))
#print(o.projection_gradient_method(m,[-1,-1],[2,2],'ball'))
#print(o.conditional_gradient_method(m,[-1,-1],[2,2],'cube'))
#print(o.conditional_gradient_method(m,[-1,-1],[2,2],'ball'))

def l(x):
    return x[0]**2

def g(x):
    return x**2

#print(o.projection_gradient_method(l,[-1],[10],'cube'))
#print(o.gradient_method(l,[-2],[1]))
#print(o.projection_gradient_method(l,[-2],[1],'cube'))
#print(o.projection_gradient_method(l,[-2],[1],'ball'))
#print(o.conditional_gradient_method(l,[-2],[1],'cube'))
#print(o.conditional_gradient_method(l,[-2],[1],'ball'))
#print(o.golden_ratio_naive(g,-2,1))

a=[[1],[2],[3],[4],[5]]
#print(a)
#print(list(np.array(a).ravel()))

# a=[-1,-1]
# b=[2,2]
# g=[1,-1]
# print(o.get_x_overline_cube(a,b,g))

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

# a=[-1,-1]
# b=[2,2]

# x0=[(i+j)/2 for i,j in zip(a,b)]
# y0=np.sqrt(sum([(i-j)**2 for (i,j) in zip(a,b)]))/2
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

a=1
b=3
c=2
#print(a)



# def f(x):
#     return x[0]**2+x[1]**2

# x = np.linspace(0, 1, 2)
# y = np.linspace(2, 3, 2)

# X, Y = np.meshgrid(x, y)
# print(X)
# print(Y)
# Z = f([X,Y])


# print(Z)



input1=input()

def a(x):
   return eval(input1)
input2=input()
input3=input()

print(o.gradient_method(a,eval(input2),eval(input3),input1))

# a=123
# print(str(a))
# fig=plt.figure(figsize=(7,7))
# x=np.linspace(-3,3,10)
# y=np.linspace(-3,3,10)
# X,Y=np.meshgrid(x,y)
# Z=k([X,Y])
# ax = plt.axes(projection='3d')
# ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='viridis',edgecolor='none')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# plt.show()

# xy_anim=[[0,0],[0,2],[2,2],[2,0]]
# z_anim=[[k(xy)] for xy in xy_anim]

# fig=plt.figure()
# ax=plt.axes(projection='3d',xlim3d=(-5,5),ylim3d=(-10,10),zlim3d=(-2,20))
# x=np.linspace(-3,3,10)
# y=np.linspace(-3,3,10)
# X,Y=np.meshgrid(x,y)
# Z=k([X,Y])
# #ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='viridis',edgecolor='none')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

# # fig = plt.figure()
# # ax = p3.Axes3D(fig)

# line, = ax.plot([],[],[],'o')
        
# def init():
#     line.set_data([],[])
#     line.set_3d_properties([],'z')
#     return line,

# def animate(i):
#     line.set_data([xy_anim[i][0]],[xy_anim[i][1]])
#     line.set_3d_properties(z_anim[i], 'z')
#     return line,

# anim=animation.FuncAnimation(fig,animate,init_func=init,frames=len(xy_anim),interval=1000,blit=True)



# plt.legend()
# plt.show()