import time
import numpy as np
size = 10000000
#checking list taken time
l1 = range(size)
l2 = range(size)
start = time.time()
result = [(x,y) for x,y in zip(l1,l2)]
print('Time taken by List:', time.time()-start)
#checking numpy array taken time
a1 = np.arange(size)
a2 = np.arange(size)
start2 = time.time()
result_numpy = a1+a2
print('Time taken by numpy:', time.time()-start2)
print("testing")