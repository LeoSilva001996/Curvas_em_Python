import numpy as np
 
U = np.array([[2.,-1.,0.],[0,3/2,-1],[0,0,4/3]])
c=np.array([1.0,1/2,2/6])
 
def SubRet(U,c):
    n=c.size
    x=np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (c[i] -U[i,i+1:]@x[i+1:])/U[i,i]
    return x

print(SubRet(U,c))