import numpy as np
from mlib2 import Opt
#a = input()

m = input()

f = lambda x: eval(m)

a = Opt()

print(a.roi(f, np.array([-2, -2]), np.array([2, 2])))