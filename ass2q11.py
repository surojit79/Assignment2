import numpy as np
import matplotlib.pyplot as plt
def f1(t,u1,u2,u3):
    return u1+2*u2-2*u3+np.exp(-t)
def f2(t,u1,u2,u3):
	return u2+u3-2*np.exp(-t)
def f3(t,u1,u2,u3):
	return u1+2*u2+np.exp(-t)
a=0
b=1
h=0.01
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
u1=np.zeros((n+1,))
u2=np.zeros((n+1,))
u3=np.zeros((n+1,))
u1[0]=3
u2[0]=-1
u3[0]=1

for i in range(n):
	k1=h*f1(t[i],u1[i],u2[i],u3[i])
	l1=h*f2(t[i],u1[i],u2[i],u3[i])
	m1=h*f3(t[i],u1[i],u2[i],u3[i])

	k2=h*f1(t[i]+0.5*h,u1[i]+0.5*k1,u2[i]+0.5*l1,u3[i]+0.5*m1)
	l2=h*f2(t[i]+0.5*h,u1[i]+0.5*k1,u2[i]+0.5*l1,u3[i]+0.5*m1)
	m2=h*f3(t[i]+0.5*h,u1[i]+0.5*k1,u2[i]+0.5*l1,u3[i]+0.5*m1)

	k3=h*f1(t[i]+0.5*h,u1[i]+0.5*k2,u2[i]+0.5*l2,u3[i]+0.5*m2)
	l3=h*f2(t[i]+0.5*h,u1[i]+0.5*k2,u2[i]+0.5*l2,u3[i]+0.5*m2)
	m3=h*f3(t[i]+0.5*h,u1[i]+0.5*k2,u2[i]+0.5*l2,u3[i]+0.5*m2)

	k4=h*f1(t[i]+h,u1[i]+k3,u2[i]+l3,u3[i]+m3)
	l4=h*f2(t[i]+h,u1[i]+k3,u2[i]+l3,u3[i]+m3)
	m4=h*f3(t[i]+h,u1[i]+k3,u2[i]+l3,u3[i]+m3)

	u1[i+1]=u1[i]+(k1+2*k2+2*k3+k4)/6
	u2[i+1]=u2[i]+(l1+2*l2+2*l3+l4)/6
	u3[i+1]=u3[i]+(m1+2*m2+2*m3+m4)/6

plt.plot(t,u1,color='r',label="u1")
plt.plot(t,u2,color='g',label="u2")
plt.plot(t,u3,color='b',label="u3")
plt.title("Runge-Kutta 4th order method")
plt.legend()
plt.grid()
plt.show()

