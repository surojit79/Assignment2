import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return (-20*(y-x)**2+2*x)
a=0 
b=1 
h= 0.0001
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
y = np.zeros((n+1,)) 
x[0]=0
y[0]=1.0/3

for j in range(n): 
    k= y[j] + h*f(x[j],y[j])
    y[j+1] = y[j] + h*f(x[j+1],k)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title( "Backward Euler's Method with h=0.0001")
plt.grid()
plt.show()

