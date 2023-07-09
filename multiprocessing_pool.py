import time
from multiprocessing import Pool
def f(n):
    sum=0
    for x in range(1000):
        sum+=x*x
    return sum

if __name__=="__main__":
    t1=time.time()
    p=Pool()
    result=p.map(f,range(100000))
    p.close()
    p.join()
    print(result)
    print("pool took time ",time.time()-t1)

    t2=time.time()
    res=[]
    for x in range(100000):
        result.append(f(x))

    print("serial processing took",time.time()-t2)