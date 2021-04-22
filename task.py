import numpy as np 
n=int(input())
a=np.array([input().split() for i in range(int(n))],int)
c=list()
b=int(len(a.flatten())/n)
for i in range(b):
    for j in range(n):
        c.append(a[j][i])
print(c)