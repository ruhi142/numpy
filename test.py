"""import numpy as np
print(np.__version__)"""

"""nums = list(range(1_000_000))
total = 0
for n in nums:
    total += n # one million Python steps
print(total)"""


"""import numpy as np
import time
nums = list(range(1_000_000))
arr = np.arange(1_000_000)
t0 = time.time(); sum(nums); print("list :", time.time()-t0)
t0 = time.time(); arr.sum(); print("numpy:", time.time()-t0)

output- list : 0.0512
numpy: 0.0006 """

""" arrays 
a = np.array([2, 4, 6, 8]) # from a list
b = np.zeros(5) # [0. 0. 0. 0. 0.]
c = np.ones((2, 3)) # 2 rows, 3 columns of 1.0
d = np.arange(0, 10, 2) # [0 2 4 6 8]
e = np.linspace(0, 1, 5) # 5 evenly spaced, 0 to 1
print(a)
print(e) 

output - [2 4 6 8]
[0. 0.25 0.5 0.75 1. ] """

