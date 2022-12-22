import numpy as np
import math
import time

class OptimizationMethods:

    def list_zero(self,a,accuracy):
        for i in range(len(a)):
            if(a[i]>=accuracy):
                return False
        return True

    def add_value(self,list,index,value):
        return list[:index]+[list[index]+value]+list[index+1:]

    def distance(self,a,b):
        return np.sqrt(sum([(x-y)**2 for (x,y) in zip(a,b)]))

    def norma(self,a):
        return np.sqrt(sum([x**2 for x in a]))

    def projection_ball(self,u,u0,R):
        if(self.distance(u,u0)<=R):
            w=u
        else:
            w=[x+(y-x)*R/self.distance(u,u0) for (x,y) in zip(u0,u)]
        return w

    def abc(self,a,b,c):
        if(a<=c<=b):
            w=c
        if(c<a):
            w=a
        if(b<c):
            w=b
        return w

    def projection_cube(self,u,a,b):
        w=[self.abc(i,j,v) for (i,j,v) in zip(a,b,u)]
        return w

    def get_x_overline_ball(self,u0,R,grad):
        w=[u-R*g/self.norma(grad) for (u,g) in zip(u0,grad)]
        return w

    def abg(self,a,b,g):
        #delta=1e-8
        if(g>=0): w=a
        if(g<0): w=b
        #if(g==0): w=(a+b)/2
        return w
    
    def get_x_overline_cube(self,a,b,grad):
        w=[self.abg(i,j,g) for (i,j,g) in zip(a,b,grad)]
        return w


    def first_derivative_1_var(self,function,point,epsilon=None):
        if(epsilon==None): epsilon=1e-8
        h=1
        diff=0
        while(abs(diff-(function(point+h)-function(point-h))/(2*h))>=epsilon):
            diff=(function(point+h)-function(point-h))/(2*h)
            h=h/2
        return diff

    def first_derivative_n_var(self,function,point,num_var,epsilon=None):
        if(epsilon==None): epsilon=1e-8
        h=1
        diff=0
        while(abs(diff-(function(self.add_value(point,num_var,h))-function(self.add_value(point,num_var,-h)))/(2*h))>=epsilon):
            diff=(function(self.add_value(point,num_var,h))-function(self.add_value(point,num_var,-h)))/(2*h)
            h=h/2
        return diff

    def gradient(self,function,point,epsilon=None):
        if(epsilon==None): epsilon=1e-8
        return [self.first_derivative_n_var(function,point,i,epsilon) for i in range(len(point))]

    def half_segment(self,function,a,b,delta=None,epsilon=None,max_iter=None):
        if(delta==None): delta=1e-8
        if(epsilon==None): epsilon=1e-8
        if(max_iter==None): max_iter=2*(int)(math.log((b-a-delta)/(epsilon-delta)))+1
        for i in range(max_iter):
            x_1=(a+b-delta)/2
            x_2=(a+b+delta)/2
            if(function(x_1)<=function(x_2)): b=x_2
            else: a=x_1
        return (x_1,function(x_1)) if function(x_1)<=function(x_2) else (x_2,function(x_2))

    def golden_ratio_naive(self,function,a,b,epsilon=None,max_iter=None):
        if(epsilon==None): epsilon=1e-8
        golden_1 = (3 - math.sqrt(5)) / 2
        golden_2 = (math.sqrt(5) - 1) / 2
        if(max_iter==None): max_iter=2*(int)(math.log(epsilon/(b-a))/math.log(golden_2))+1
        for i in range(max_iter):
            x_1=a+(b-a)*golden_1
            x_2=a+(b-a)*golden_2
            if(function(x_1)<=function(x_2)): 
                b=x_2
                x=x_1
            else: 
                a=x_1
                x=x_2
        return (a+b-x,function(a+b-x)) if function(a+b-x)<=function(x) else (x,function(x))
 
    def gradient_method(self,function,a,b,epsilon=None,delta=None):
        if(epsilon==None): epsilon=1e-8
        if(delta==None): delta=1e-8
        x0=[(i+j)/2 for i,j in zip(a,b)]
        delta1=[1]*len(x0)
        iter=0
        while(self.list_zero(self.gradient(function,x0),epsilon)==False and self.list_zero(delta1,delta)==False):
            #print(iter)
            iter=iter+1
            def func1(a):
                return function([x-a*y for (x,y) in zip(x0,self.gradient(function,x0))])
            alpha=self.golden_ratio_naive(func1,0,1000)[0]
            result=[x-alpha*y for (x,y) in zip(x0,self.gradient(function,x0))]
            delta1=[abs(x-y) for (x,y) in zip(x0,result)]
            x0=result
        return (x0,function(x0))
    
    def projection_gradient_method(self,function,a,b,method,epsilon=None,delta=None):
        x0=[(x+y)/2 for x,y in zip(a,b)]
        if(epsilon==None): epsilon=1e-8
        if(delta==None): delta=1e-8
        if(method=='cube'): 
            proj=self.projection_cube
            m1=a
            m2=b
        if(method=='ball'): 
            proj=self.projection_ball
            m1=x0
            m2=self.distance(a,b)/2
        delta1=[1]*len(x0)
        iter=0
        while(self.list_zero(self.gradient(function,x0),epsilon)==False and self.list_zero(delta1,delta)==False):
            #print(iter)
            iter=iter+1
            def func1(a):
                u=[x-a*y for (x,y) in zip(x0,self.gradient(function,x0))]
                return function(proj(u,m1,m2))
            alpha=self.golden_ratio_naive(func1,0,1000)[0]
            u=[x-alpha*y for (x,y) in zip(x0,self.gradient(function,x0))]
            result=proj(u,m1,m2)
            delta1=[abs(x-y) for (x,y) in zip(x0,result)]
            x0=result
        return (x0,function(x0))

    def conditional_gradient_method(self,function,a,b,method,epsilon=None,delta=None):
        x0=[(x+y)/2 for x,y in zip(a,b)]
        if(epsilon==None): epsilon=1e-8
        if(delta==None): delta=1e-8
        if(method=='cube'): 
            m1=a
            m2=b
            overline=self.get_x_overline_cube
        if(method=='ball'):
            m1=x0
            m2=self.distance(a,b)/2
            overline=self.get_x_overline_ball
        delta1=[1]*len(x0)
        delta2=[1]*len(x0)
        delta3=[1]*len(x0)
        iter=0
        while(self.list_zero(self.gradient(function,x0),epsilon)==False and self.list_zero(delta1,delta)==False):
            #print(iter)
            iter=iter+1
            x_overline=overline(m1,m2,self.gradient(function,x0))
            #print(delta2,'delta2')
            #delta2=[abs(x-y) for (x,y) in zip(x0,x_overline)]
            #if(self.list_zero(delta2,delta)==True): break
            #print(self.gradient(function,x0),'grad')
            #print(x0,'x0')
            #print(x_overline,'x_over')
            def func1(a):
                u=[x+a*(y-x) for (x,y) in zip(x0,x_overline)]
                return function(u)
            alpha=self.golden_ratio_naive(func1,0,1)[0]
            #print(alpha,'alpha')
            result=[x+alpha*(y-x) for (x,y) in zip(x0,x_overline)]
            #print(result,'result')
            delta1=[abs(x-y) for (x,y) in zip(x0,result)]
            #print(delta1,'delta1')
            #delta3==[abs(x-y) for (x,y) in zip(result,x_overline)]
            #print(delta3,'delta3')
            #print(self.list_zero([abs(x-y) for (x,y) in zip(self.gradient(function,x0),self.gradient(function,result))],epsilon))
            #if(self.list_zero([abs(x-y) for (x,y) in zip(self.gradient(function,x0),self.gradient(function,result))],epsilon)==True): break
            x0=result
            #if(self.list_zero(delta3,delta)==True): break
        return (x0,function(x0))


