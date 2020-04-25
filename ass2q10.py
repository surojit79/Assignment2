import numpy as np
import matplotlib.pyplot as plt
def f(u,x):
	return 1/(u**2+x**2*(1-u)**2)
	
a=0
b=1
h=0.01
n=int((b-a)/h)
u=np.linspace(0,1,n+1)		
x=np.zeros((n+1),)		
x[0]=1
for i in range(n):
	k1=h*f(u[i],x[i])
	k2=h*f(u[i]+0.5*h,x[i]+0.5*k1)
	k3=h*f(u[i]+0.5*h,x[i]+0.5*k2)
	k4=h*f(u[i]+h,x[i]+k3)
	x[i+1]=x[i]+(k1+2*k2+2*k3+k4)/6

t=u/(1-u) 		
print('x(t=3.5*10**(6))=',x[n])
plt.xlabel("t")
plt.ylabel("x")
plt.plot(t,x)
plt.plot(t,x,'g')
plt.legend()
plt.grid()
plt.show()
