import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Opt():

    def animate_3D(self, fun: 'function', x_anim: np.array, x_min: np.array, x_max: np.array) -> None:
        
        y_anim = np.array([[fun(x) for x in x_anim_i] for x_anim_i in x_anim])
        #print(x_anim)
        #print(x_anim.shape)
        #print(y_anim)
        #print(y_anim.shape)

        fig = plt.figure()
        ax = plt.axes(projection = '3d')
        x = np.linspace(x_min[0], x_max[0], 50)
        y = np.linspace(x_min[1], x_max[1], 50)
        X, Y = np.meshgrid(x, y)
        Z = fun([X, Y])
        
        surf = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, edgecolor = 'none')
        surf._edgecolors2d = surf._edgecolor3d
        surf._facecolors2d = surf._facecolor3d
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')


        lines = []

        for i in range(x_anim.shape[1]):
            line, = ax.plot([], [], [], 'o', color = 'r')
            lines.append(line)
        #print(len(lines))

        def init():
            for line in lines:
                line.set_data([], [])
                line.set_3d_properties([],'z')
            return lines
        
        def animate(i):
            for j in range(x_anim.shape[1]):
                #print(x_anim[i][j][0], x_anim[i][j][1], y_anim[i][j])
                lines[j].set_data(x_anim[i][j][0], x_anim[i][j][1])
                lines[j].set_3d_properties(y_anim[i][j], 'z')
                #print(lines[j])
            return lines
        
        # for i in range(x_anim.shape[0]):
        #     animate(i)
        #     print(lines)
        
        anim = animation.FuncAnimation(fig, animate, init_func = init, frames = x_anim.shape[0], interval = 100, blit = True)
        #plt.legend()
        plt.show()


    def roi(self, fun: 'function', x_min: np.array, x_max: np.array) -> float:

        k, r_p, r_g = np.random.uniform(0, 1, 3)

        phi_p,  phi_g = np.random.uniform(2, 3, 2)
        phi = phi_p + phi_g

        chi = 2 * k / abs(2 - phi - np.sqrt(phi ** 2 - 4 * phi))

        N = 50 #how many points

        x_anim = []

        x = np.array([np.random.uniform(mi, ma, N) for (mi, ma) in zip(x_min, x_max)])
        x = np.transpose(x)
        #print(x)

        x_anim.append(x)
        #print(x_anim)

        v = np.array([np.random.uniform(mi, ma, N) for (mi, ma) in zip(- (x_max - x_min), (x_max - x_min))])
        v = np.transpose(v)
        mem = np.array([x_i if fun(x_i) <= fun(x_i + v_i) else x_i + v_i for (x_i, v_i) in zip(x, v)])
        best = sorted(mem, key = lambda x: fun(x))[0]
        best_y = fun(best)
        x = x + v
        x_anim.append(x)
        #print(x_anim)

        #here is loop start
        for i in range(100):

            v = np.array([chi * (v_i + phi_p * r_p * (mem_i - x_i) + phi_g * r_g * (best - x_i)) for (v_i, x_i, mem_i) in zip(v, x, mem)])
            
            x = x + v
            x_anim.append(x)
            
            mem = np.array([x_i if fun(x_i) <= fun(mem_i) else mem_i for (x_i, mem_i) in zip(x, mem)])
            best = sorted(mem, key = lambda x: fun(x))[0]
            best_y = min(best_y, fun(best))

        x_anim = np.array(x_anim)
        #print(x_anim)
        #print(x_anim.shape)
        self.animate_3D(fun, x_anim, x_min, x_max)

        return best_y

        




