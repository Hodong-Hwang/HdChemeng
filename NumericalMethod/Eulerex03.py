
import numpy as np 
import matplotlib.pyplot as plt

def rhs(t,yvec):
    mu = 1 
    dy =np.zeros(2)
    dy[0] = dy[0] = mu*(1-yvec[1]**2)*yvec[0]-yvec[1]
    dy[1] = yvec[0]
    return dy

a = 0
b = 20
n = 500
dt = (b-a)/n

t=np.arange(a,b+dt,dt)
y = np.zeros((n+1,2))


y[0,0] = 1
y[0,1] = 1
for k in np.arange(1,n+1,1):
    dy = rhs(t[k-1],y[k-1,:])
    y[k,:] = dy*dt+y[k-1,:]
    
    
plt.plot(t,y[:,0])
plt.plot(t,y[:,1])
plt.autoscale(enable=True, axis='x', tight=True)
plt.xlabel('t')
plt.grid()
plt.legend(['x(t)','y(t)'])
plt.figure()
plt.plot(y[:,0],y[:,1])
head = 1
tail = 0

w = int(n/12)
dx = y[head,0]-y[tail,0]
dy = y[head,1]-y[tail,1]
plt.arrow(y[head,0],y[head,1],dx,dy,width=.01)
numarrows = int((n-head)/w)
for i in range(4):
    head = head + w
    tail = tail + w 
    dx = y[head,0]-y[tail,0]
    dy = y[head,1]-y[tail,1]
    plt.arrow(y[head,0],y[head,1],dx,dy,width=.025)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('Phase Portrait: IC = (1,1)')
plt.grid()
plt.show()
