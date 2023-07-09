import numpy as np
import time
import sys

SIZE=100000000
l=range(1000)
print(sys.getsizeof(5)*len(l))

array=np.arange(1000)
print(array.size*array.itemsize)

l1=range(SIZE)
l2=range(SIZE)

a1=np.arange(SIZE)
a2=np.arange(SIZE)

start=time.time()
result=[(x+y) for x,y in zip(l1,l2)]
print("python list took :- ",(time.time()-start)*1000);

start2=time.time()
result2=a1+a2
print("numpy list took :- ",(time.time()-start2)*1000);