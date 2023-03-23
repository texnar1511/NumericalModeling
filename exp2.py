import numpy as np
from mlib2 import Opt
#a = input()

m = input()

f = lambda x: eval(m)

a = Opt()

print(a.roi(f, np.array([-1, -1]), np.array([1, 1])))