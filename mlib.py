import numpy as np
import math

class MathObjects:

    def first_derivate(function,point,epsilon=None):
        if(epsilon==None): epsilon=1e-6
        h=1
        diff=(function(point+h)-function(point))/h
        h=h/2
        while(abs(diff-(function(point+h)-function(point))/h)>=epsilon):
            diff=(function(point+h)-function(point))/h
            h=h/2
        return diff

class OptimizationMethods:

    def half_segment(function,a,b,delta=None,epsilon=None,max_iter=None):
        if(delta==None): delta=1e-7
        if(epsilon==None): epsilon=1e-6
        if(max_iter==None): max_iter=2*(int)(math.log((b-a-delta)/(epsilon-delta)))+1
        for i in range(max_iter):
            x_1=(a+b-delta)/2
            x_2=(a+b+delta)/2
            if(function(x_1)<=function(x_2)): b=x_2
            else: a=x_1
        return min(function(x_1),function(x_2))

    def golden_ration_naive(function,a,b,epsilon=None,max_iter=None):
        if(epsilon==None): epsilon=1e-6
        golden_1 = (3 - math.sqrt(5)) / 2
        golden_2 = (math.sqrt(5) - 1) / 2
        if(max_iter==None): max_iter=(int)(math.log(epsilon/(b-a))/math.log(golden_2))+1
        for i in range(max_iter):
            x_1=a+(b-a)*golden_1
            x_2=a+(b-a)*golden_2
            if(function(x_1)<=function(x_2)): 
                b=x_2
                x=x_1
            else: 
                a=x_1
                x=x_2
        return min(function(a+b-x),function(x))

    def gradient_iter(function,a,b,delta=None,epsilon=None,max_iter=None):
        
        return 0