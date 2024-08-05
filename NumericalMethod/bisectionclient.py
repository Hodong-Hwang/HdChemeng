from bisection import *

def shifted_exp(x):
    y = np.exp(x) - 3
    return y

tol = 0.0001
a = 1 
b = 2

x= bisect(shifted_exp,a,b,tol)
print('final x =',x)
print('final f(x) =',shifted_exp(x))