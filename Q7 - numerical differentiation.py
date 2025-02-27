import numpy as np
import matplotlib.pyplot as plt

deltaT = 0.01
T = np.arange(0,20,deltaT)
x = np.zeros(len(T))
x[0] = x[1] = 0.01

def F(v,f):
    if v < 0:
        return f
    elif v > 0:
        return -f
    else:
        return 0

def NumericalDifferentiation(dt, m, k , f, x):
    for i in range(2, len(x)):
        v = (x[i-1]-x[i-2])/(dt)
        x[i] = (dt**2)*F(v,f)/m - ((dt**2)*k/(m))*x[i-1] + 2*x[i-1] - x[i-2]
    return x

    
    
y = NumericalDifferentiation(deltaT, 1, 40, 0, x)
plt.plot(T, y, label = "Numerical")
plt.plot(T, 0.01*np.cos(np.sqrt(40/1)*T), label="analytical")
plt.xlabel('$t$') 
plt.ylabel('$x$') 


y2 = NumericalDifferentiation(deltaT, 1, 40, 0.025, x)
plt.plot(T, y2, label = "Numerical f=0.025")
plt.legend() 
