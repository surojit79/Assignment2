import numpy as np 
import matplotlib.pyplot as plt 
def f1(t,u,y):
	return (t*np.log(t)+2*u/t-2*y/t**2)
def f2(u):
	return (u)
def f3(t):
	return (7*t/4.0+t**3/2*np.log(t)-3/4.0*t**3)
a=1
b=2
h=0.001
n=int((b-a)/h)
t=np.linspace(a,b,n+1)	
y=np.zeros((n+1),)
u=np.zeros((n+1),)
yexact=np.zeros((n+1),)
y[0]=1
u[0]=0
for i in range(n):
	u[i+1]=u[i]+h*f1(t[i],u[i],y[i]) 
	y[i+1]=y[i]+h*(f2(u[i])+f2(u[i+1]))/2

for j in range(n):
	yexact[j]=f3(t[j])
	
plt.plot(t,y,'g-o',label="Euler method")
plt.plot(t,yexact,'r',label="exact solution")
plt.xlabel(r'$t$',fontsize=26)
plt.ylabel(r'$y$',fontsize=26)	
plt.legend()
plt.grid()
plt.show()
