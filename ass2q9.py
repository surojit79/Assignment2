import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f1(t,y):
	return (y**2+y)/t

def f2(u,t):
    return ((u**2+u)/t)
h=0.01
dh=10**(-5)

t0=1.0
w=-2.0 
y=np.array([-2.0])
t=np.array([1.0])

tf=1
while (tf<=3.0):
    
    k1=h*f1(t0,w)
    k2=h*f1(t0+h/2,w+k1/2)
    k3=h*f1(t0+h/2,w+k2/2)
    k4=h*f1(t0+h,w+k3)

    l1=2*h*f1(t0,w)
    l2=2*h*f1(t0+h,w+l1/2)
    l3=2*h*f1(t0+h,w+l2/2)
    l4=2*h*f1(t0+2*h,w+l3)
   
    y2=w+1/6*(l1+2*l2+2*l3+l4)	
    w=w+1/6*(k1+2*k2+2*k3+k4)
    t0=t0+h
    y=np.append(y,w)
    t=np.append(t,t0)

    k1=h*f1(t0,w)
    k2=h*f1(t0+h/2,w+k1/2)
    k3=h*f1(t0+h/2,w+k2/2)
    k4=h*f1(t0+h,w+k3)

    y1=w+1/6*(k1+2*k2+2*k3+k4)

    h=h*(dh*30/(abs(y1-y2)))**0.25

    tf=t0

yt=odeint(f2,y[0],t)
error=np.zeros(len(t))
for i in range(len(error)):
	error[i]=abs(y[i]-yt[i])
abserror=max(error)
print(" absolute error is",abserror)
plt.xlabel("t")
plt.ylabel("y")
plt.plot(t,y,'r-o',label = "Adaptive step size control")
plt.plot(t,yt,'g-o',label="exact solution")
plt.legend()
plt.grid()
plt.show()

