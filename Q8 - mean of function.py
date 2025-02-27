import numpy as np
import random
import math

x = np.array
def MonteCarlo(N, a, b):
    Sum = 0
    for i in range(0,N):
        Sum += f2(random.uniform(-a,a),random.uniform(-b,b))
    return 4*a*b*Sum/N

def f(x,y):
    return (np.exp(x*y))*np.power(np.cos(y),2)*np.sin(x**2)

def f2(x,y):
    if(x**2 + y**2)<=1:
        return 1
    else:
        return 0

pi = MonteCarlo(10**2,1,1)
print("100:", pi)
print("Absolute error:", np.abs(np.pi - pi))

pi = MonteCarlo(10**5,1,1)
print("100000:", pi)
print("Absolute error:", np.abs(np.pi - pi))

pi = MonteCarlo(10**6,1,1)
print("1000000:", pi)
print("Absolute error:", np.abs(np.pi - pi))