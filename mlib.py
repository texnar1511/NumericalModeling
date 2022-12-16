import numpy as np
import math

class OptimizationMethods:

    def gradient_zero(self,grad,epsilon):
        for i in range(len(grad)):
            if(grad[i]>=epsilon):
                return False
        return True

    def add_value(self,list,index,value):
        return list[:index]+[list[index]+value]+list[index+1:]

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
        if(delta==None): delta=1e-9
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
 
    def gradient_method(self,function,a,b,epsilon=None):
        if(epsilon==None): epsilon=1e-8
        x0=[(i+j)/2 for i,j in zip(a,b)]
        while(self.gradient_zero(self.gradient(function,x0),epsilon)==False):
            #print(self.gradient(function,x0),'grad')
            #print(self.gradient_zero(self.gradient(function,x0),epsilon))
            #print(x0,'x0')
            def g_k(a_k):
                #print(x0)
                return function([x-a_k*y for (x,y) in zip(x0,self.gradient(function,x0))])
            #print(g_k(1))
            alpha=self.golden_ratio_naive(g_k,0,100)
            #print(alpha)
            x0=[x-alpha[0]*y for (x,y) in zip(x0,self.gradient(function,x0))]
        return (x0,function(x0))