import matplotlib.pyplot as plt
import numpy as np
def f(y,u,x):
	return 2*u-y+x*np.exp(x)-x
def g(u):
	return u
a=0 
b=1 
h= 0.01 
n=int((b-a)/h)
x=np.linspace(a,b,n+1)

u = np.zeros((n+1,))
y = np.zeros((n+1,))
u[0]=0
y[0]=0

for j in range(n):
    k1=h*f(y[j],u[j],x[j])
    m1=h*g(u[j])
    k2=h*f(y[j]+0.5*m1,u[j]+0.5*k1,x[j]+0.5*h)
    m2=h*g(u[j]+0.5*k1)
    k3=h*f(y[j]+0.5*m2,u[j]+0.5*k2,x[j]+0.5*h)
    m3=h*g(u[j]+0.5*k2)
    k4=h*f(y[j]+m3,u[j]+k3,x[j]+h)
    m4=h*g(u[j]+k3)
    u[j+1]=u[j]+(k1+2*k2+2*k3+k4)/6
    y[j+1]=y[j]+(m1+2*m2+2*m3+m4)/6

plt.xlabel("x")
plt.ylabel("y")
plt.title("Runge-Kutta 4th order method")
plt.plot(x,y)
plt.show()	

