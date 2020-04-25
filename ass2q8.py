import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt
#Sol1
def f1(x, y):
        return np.vstack((y[1], -np.exp(-2*y[0])))

def bc1(ya, yb):
	return np.array([ya[0], yb[0]-np.log(2)])

x = np.linspace(1,2)
y1 = np.zeros((2, x.size))
Sol = scint.solve_bvp(f1, bc1, x, y1)
y = np.log(x)#exact solution
plt.plot(x,Sol.sol(x)[0],'g-o',x,y,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#Sol2
def f2(x, y):
	return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))

def bc2(ya, yb):
	return np.array([ya[0]-1, yb[0]-np.exp(1)])

x = np.linspace(0, np.pi/2)
y2 = np.zeros((2, x.size))
y2[0]=1
Sol= scint.solve_bvp(f2, bc2, x, y2)
y = np.exp(np.sin(x))#exact solution
plt.plot(x,Sol.sol(x)[0],'g-o',x,y,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#Sol3
def f3(x, y):
	return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*np.cos(x)**(-1) ))

def bc3(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])

x = np.linspace(np.pi/4, np.pi/3)
y3 = np.zeros((2, x.size))
y3[0]=2**(-1/4)
Sol = scint.solve_bvp(f3, bc3, x, y3)
y = np.sqrt(np.sin(x))#exact solution
plt.plot(x,Sol.sol(x)[0],'g-o',x,y,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#Sol4
def f4(x, y):
	return np.vstack((y[1], 0.5*(1-y[1]**2-y[0]*np.sin(x))  ))

def bc4(ya, yb):
	return np.array([ya[0]-2, yb[0]-2 ])

x = np.linspace(0, np.pi)
y4 = np.zeros((2, x.size))
y4[1]=1
Sol = scint.solve_bvp(f4, bc4, x, y3)
y = 2+np.sin(x)#exact solution
plt.plot(x,Sol.sol(x)[0],'g-o',x,y,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
