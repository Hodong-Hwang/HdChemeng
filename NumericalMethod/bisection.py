import numpy as np
def bisect (f,a,b,tol):
    x=(a+b)/2
    while np.abs(f(x))>tol :
        print('a={:.5f} f(a)={:.5f}, b={:.5f} f(b)={:.5f},)x={:.5f} f(x)={:.5f}'.format(a,f(a),b,f(b),x,f(x)))
        if f(a)*f(x) < 0:
            b=x
        elif f(b)*f(x) < 0 :
            a=x
        x=(a+b)/2
    return x