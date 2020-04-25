import numpy as np 
import matplotlib.pyplot as plt 
def f(x,z,t):
	return -10  #f(x,z,t)=dz/dt
def g(z):
	return z    #g(z)=dx/dt=z
a=0
b=10
h= 0.1
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
x=np.zeros((n+1,))
z=np.zeros((n+1,))
#Given
x[0]=0
u=40#guess from the exact solution
v=60
count=1
while 2==2:
    z[0]=(u+v)*0.5
    for i in range(n):
        k1=h*f(x[i],z[i],t[i])
        l1=h*g(z[i])
        k2=h*f(x[i]+l1*0.5,z[i]+k1*0.5,t[i]+h*0.5)
        l2=h*g(z[i]+k1*0.5)
        k3=h*f(x[i]+l2*0.5,z[i]+k2*0.5,t[i]+h*0.5)
        l3=h*g(z[i]+k2*0.5)
        k4=h*f(x[i]+l3,z[i]+k3,t[i]+h)
        l4=h*g(z[i]+k3)
        z[i+1]=z[i]+(k1+k2*2+k3*2+k4)/6
        x[i+1]=x[i]+(l1+l2*2+l3*2+l4)/6
    count=x[n]
    if abs(count)<=0.00001:
        break
    if count>0:
        u=z[0]
    else:
        v=z[0]
    plt.plot(t,x,'b')
plt.plot(t,x,'g-o')

xexact=np.zeros((n+1,))

for j in range(n):
    xexact[j]=-5*(t[j]-10)*t[j]
plt.plot(t,xexact,color='r',label="exact solution")	
plt.xlabel('t')
plt.ylabel('x')
plt.title('Shooting method') 		
plt.legend()
plt.show()	






