import numpy as np 
import matplotlib.pyplot as plt

def rhs(t,yvec):
    dy = np.zeros(2)
    dy[0] = yvec[1]**2-yvec[0]
    dy[1] = (yvec[1]-yvec[0]/2)
    return dy


a = 0
b = 20

n = 500

dt =(b-a)/n

t = np.arange(a,b+dt,dt)
y = np.zeros((n+1,2))
i = np.arange(1,n+1,1)
y[0,0] = 1.5
y[0,1] = 1


for k in i :
    dy = rhs(t[k-1],y[k-1,:])
    y[k,:] = dy*dt+y[k-1,:]
    
plt.plot(t,y[:,0])
plt.plot(t,y[:,1])
plt.autoscale(enable=True, axis='x', tight=True)
plt.xlabel('t')
plt.grid()
plt.legend(['x(t)','y(t)'])
plt.show()