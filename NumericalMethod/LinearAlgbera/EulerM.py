import numpy as np 
import matplotlib.pyplot as plt 

def rhs(t,y):
    m = (y-t)/2
    return m

a = 0 
b = 5
n = 10
dt = (b-a) / n

t = np.arange(a,b+dt,dt)

print(t)
y = np.zeros(n+1)
i = np.arange(1,1+n,1)

y[0]= 1

for k in i :
    m = rhs(t[k-1],y[k-1])
    y[k] = m*dt+y[k-1]
    
plt.plot(t,y)
plt.autoscale(enable=True, axis='x', tight=True)
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.show()