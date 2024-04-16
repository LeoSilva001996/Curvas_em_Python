import numpy as np


def SubRet(U,c):
    n=c.size
    x=np.zeros(n)
    for i in reversed(range(n)):
         x[i] = (c[i] -U[i,i+1:]@x[i+1:])/U[i,i]
    return x
