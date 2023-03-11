import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class OptimizationMethods:

    def animation_2D(self,function,x_anim,labels):
        #print(x_anim)
        #x_anim = [[x1, x2, x3, x4, ...], [y1, y2, y3, y4, ...], ...]
        y_anim = [[function(x) for x in x_anim_i] for x_anim_i in x_anim]
        #print(y_anim)
        fig=plt.figure()
        x_flat = [item for sublist in x_anim for item in sublist]
        y_flat = [item for sublist in y_anim for item in sublist]
        delt=abs(max(x_flat)-min(x_flat))/5
        eps=abs(max(y_flat)-min(y_flat))/5
        x_lim=[min(x_flat)-delt,max(x_flat)+delt]
        y_lim=[min(y_flat)-eps,max(y_flat)+eps]
        ax=plt.axes(xlim=x_lim,ylim=y_lim)
        lines = []
        for i in range(len(x_anim)):
            if(i == 0): col = 'b'
            if(i == 1): col = 'g'
            if(i == 2): col = 'r'
            line, = ax.plot([],[],'o',color = col, label = labels[i])
            lines.append(line)
        
        def init():
            for line in lines:
                line.set_data([],[])
            return lines

        def animate(i):
            for j in range(len(x_anim)):
                lines[j].set_data(x_anim[j][i], y_anim[j][i])
            return lines
        
        linsp=list(np.linspace(min(x_flat)-delt,max(x_flat)+delt,1000))
        ax.plot(linsp,[function(x) for x in linsp], color = 'y' , label = 'func')
        anim=animation.FuncAnimation(fig,animate,init_func=init,frames=len(x_anim[0]), interval = 1000, blit=True)
        plt.legend()
        plt.show()

    def animate_optimization_2D(self,function,x_anim,label1,label2):
        #print(x_anim)
        y_anim=[[function(x)] for x in x_anim]
        #print(y_anim)
        fig=plt.figure()
        x_flat=list(np.array(x_anim).ravel())
        y_flat=list(np.array(y_anim).ravel())
        delt=abs(max(x_flat)-min(x_flat))/5
        eps=abs(max(y_flat)-min(y_flat))/5
        x_lim=[min(x_flat)-delt,max(x_flat)+delt]
        y_lim=[min(y_flat)-eps,max(y_flat)+eps]
        ax=plt.axes(xlim=x_lim,ylim=y_lim)
        line, = ax.plot([],[],'o',color='r',label=label2)
        
        def init():
            line.set_data([],[])
            return line,

        def animate(i):
            line.set_data(x_anim[i],y_anim[i])
            return line,
        
        linsp=list(np.linspace(min(x_flat)-delt,max(x_flat)+delt,1000))
        ax.plot(linsp,[function([x]) for x in linsp],color='b',label=label1)
        anim=animation.FuncAnimation(fig,animate,init_func=init,frames=len(x_anim), interval = 2000,blit=True)
        plt.legend()
        plt.show()

    def animate_optimization_3D(self,function,xy_anim,label1,label2):
        z_anim=[[function(xy)] for xy in xy_anim]
        x_anim=[[xy[0]] for xy in xy_anim]
        y_anim=[[xy[1]] for xy in xy_anim]
        x_flat=list(np.array(x_anim).ravel())
        y_flat=list(np.array(y_anim).ravel())
        z_flat=list(np.array(z_anim).ravel())
        delt1=abs(max(x_flat)-min(x_flat))/5
        delt2=abs(max(y_flat)-min(y_flat))/5
        eps=abs(max(z_flat)-min(z_flat))/5
        x_lim=[min(x_flat)-delt1,max(x_flat)+delt1]
        y_lim=[min(y_flat)-delt2,max(y_flat)+delt2]
        z_lim=[min(z_flat)-eps,max(z_flat)+eps]

        fig=plt.figure()
        ax=plt.axes(projection='3d',xlim3d=x_lim,ylim3d=y_lim,zlim3d=z_lim)
        x=np.linspace(min(x_flat)-delt1,max(x_flat)+delt1,30)
        y=np.linspace(min(y_flat)-delt2,max(y_flat)+delt2,30)
        X,Y=np.meshgrid(x,y)
        Z=function([X,Y])
        surf=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,edgecolor='none',label=label1)
        surf._edgecolors2d=surf._edgecolor3d
        surf._facecolors2d=surf._facecolor3d
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        line, = ax.plot([],[],[],'o',color='r',label=label2)

        def init():
            line.set_data([],[])
            line.set_3d_properties([],'z')
            return line,

        def animate(i):
            line.set_data([xy_anim[i][0]],[xy_anim[i][1]])
            line.set_3d_properties(z_anim[i], 'z')
            return line,
        
        anim=animation.FuncAnimation(fig,animate,init_func=init,frames=len(xy_anim),interval=1000,blit=True)
        ax.legend()
        plt.legend()
        plt.show()

    def animation(self):
        
        x, y = np.mgrid[-5:5:0.05, -5:5:0.05]
        z = (np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2))

        fig, ax = plt.subplots(1,1)
        im = ax.imshow(z)
        fig.colorbar(im)
        ax.yaxis.set_major_locator(plt.NullLocator()) # remove y axis ticks
        ax.xaxis.set_major_locator(plt.NullLocator()) # remove x axis ticks
        plt.show()

    def list_zero(self,a,accuracy):
        for i in range(len(a)):
            if(abs(a[i])>=accuracy):
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


    def half_segment(self, function, a, b, delta = None, epsilon=None,max_iter=None):
        if(delta==None): delta=1e-8
        if(epsilon==None): epsilon=1e-7
        if(max_iter==None): max_iter=2*(int)(math.log((b-a-delta)/(epsilon-delta))) + 1
        #print(max_iter)
        x_anim = [[a], [b]]
        for i in range(max_iter):
            x_1=(a+b-delta)/2
            x_2=(a+b+delta)/2
            if(function(x_1)<=function(x_2)): b=x_2
            else: a=x_1
            x_anim[0].append(a)
            x_anim[1].append(b)
            #x_anim[2].append((a + b) / 2)
        #print(x_anim)
        self.animation_2D(function, x_anim, ['a', 'b'])
        return (x_1,function(x_1)) if function(x_1)<=function(x_2) else (x_2,function(x_2))
    
    
    def golden_ratio_naive(self,function,a,b,epsilon=None,max_iter=None):
        if(epsilon==None): epsilon=1e-8
        golden_1 = (3 - math.sqrt(5)) / 2
        golden_2 = (math.sqrt(5) - 1) / 2
        if(max_iter==None): max_iter=2*(int)(math.log(epsilon/(b-a))/math.log(golden_2))+1
        x_anim = [[a], [b], [(a + b) / 2]]
        for i in range(max_iter):
            x_1=a+(b-a)*golden_1
            x_2=a+(b-a)*golden_2
            if(function(x_1)<=function(x_2)): 
                b=x_2
                x=x_1
            else: 
                a=x_1
                x=x_2
            x_anim[0].append(a)
            x_anim[1].append(b)
            x_anim[2].append(x)
        self.animation_2D(function, x_anim, ['a', 'b', 'x'])
        #self.animate_optimization_2D(function,x_anim,label,str(([round(x,2) for x in x0],round(function(x0),2))))
        return (a+b-x,function(a+b-x)) if function(a+b-x)<=function(x) else (x,function(x))
 
    def gradient_method(self,function,a,b,label = None,initial_point=None,epsilon=None,delta=None):
        if(epsilon==None): epsilon=1e-8
        if(delta==None): delta=1e-8
        x0=initial_point
        if(initial_point==None): x0=[(i+j)/2 for i,j in zip(a,b)]
        x_anim=[x0]
        delta1=[1]*len(x0)
        iter=0
        while(self.list_zero(self.gradient(function,x0),epsilon)==False and self.list_zero(delta1,delta)==False):
            #print(iter)
            iter=iter+1
            #print(self.gradient(function,x0))
            def func1(a):
                return function([x-a*y for (x,y) in zip(x0,self.gradient(function,x0))])
            alpha = self.golden_ratio_naive(func1, 0, 1000)[0]
            result=[x-alpha*y for (x,y) in zip(x0,self.gradient(function,x0))]
            delta1=[abs(x-y) for (x,y) in zip(x0,result)]
            x0=result
            x_anim.append(x0)
        #print(x_anim)
        #animation
        #if(len(a)==1): self.animate_optimization_2D(function,x_anim,label,str(([round(x,2) for x in x0],round(function(x0),2))))
        #if(len(a)==2): self.animate_optimization_3D(function,x_anim,label,str(([round(x,2) for x in x0],round(function(x0),2))))
        return (x0,function(x0))
    
    def projection_gradient_method(self,function,a,b,label,method,initial_point=None,epsilon=None,delta=None):
        x0=initial_point
        if(initial_point==None): x0=[(i+j)/2 for i,j in zip(a,b)]
        x_anim=[x0]
        if(epsilon==None): epsilon=1e-8
        if(delta==None): delta=1e-8
        if(method=='cube'): 
            proj=self.projection_cube
            m1=a
            m2=b
        if(method=='ball'): 
            proj=self.projection_ball
            m1=[(x+y)/2 for x,y in zip(a,b)]
            m2=self.distance(a,b)/2
        delta1=[1]*len(x0)
        iter=0
        while(self.list_zero(self.gradient(function,x0),epsilon)==False and self.list_zero(delta1,delta)==False):
            print(iter)
            iter=iter+1
            def func1(a):
                u=[x-a*y for (x,y) in zip(x0,self.gradient(function,x0))]
                return function(proj(u,m1,m2))
            alpha=self.golden_ratio_naive(func1,0,1000)[0]
            u=[x-alpha*y for (x,y) in zip(x0,self.gradient(function,x0))]
            result=proj(u,m1,m2)
            delta1=[abs(x-y) for (x,y) in zip(x0,result)]
            x0=result
            x_anim.append(x0)
        #print(x_anim,'x_anim')
        #animation
        #if(len(a)==1): self.animate_optimization_2D(function,x_anim,label,str(([round(x,2) for x in x0],round(function(x0),2))))
        #if(len(a)==2): self.animate_optimization_3D(function,x_anim,label,str(([round(x,2) for x in x0],round(function(x0),2))))
        return (x0,function(x0))

    def conditional_gradient_method(self,function,a,b,label,method,initial_point=None,epsilon=None,delta=None):
        x0=initial_point
        if(initial_point==None): x0=[(i+j)/2 for i,j in zip(a,b)]
        x_anim=[x0]
        if(epsilon==None): epsilon=1e-8
        if(delta==None): delta=1e-8
        if(method=='cube'): 
            m1=a
            m2=b
            overline=self.get_x_overline_cube
        if(method=='ball'):
            m1=[(x+y)/2 for x,y in zip(a,b)]
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
            x_anim.append(x0)
        #animation
        #if(len(a)==1): self.animate_optimization_2D(function,x_anim,label,str(([round(x,2) for x in x0],round(function(x0),2))))
        #if(len(a)==2): self.animate_optimization_3D(function,x_anim,label,str(([round(x,2) for x in x0],round(function(x0),2))))
        return (x0,function(x0))

    def swarm_particles_method(self,function,a,b):
        plt.plot(np.random.normal())
        plt.ylabel('some numbers')
        plt.show()
        return 0