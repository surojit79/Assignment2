from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
# ODE1 
def f1(t,y):
      return (t*np.exp(3*t)-2*y)
   #exact solution is
def exact1(t):
      return ((5*t-1)*np.exp(3*t)/25+np.exp(-2*t)/25)


t=np.linspace(0,1)
sol=solve_ivp(f1,[0,1],[0],t_eval=np.linspace(0,1))

y1=exact1(t)
plt.plot(sol.t,sol.y[0],'r-o',t,y1,'g')
plt.xlabel('t')
plt.ylabel('y')
plt.show()

# ODE2
def f2(t,y):
      return (1-(t-y)**2)
   #exact solution is
def exact2(t):
      return((1-3*t+t**2)/(-3+t))


t=np.linspace(2,3)
sol=solve_ivp(f2,[2,3],[1],t_eval=np.linspace(2,3))

y2=exact2(t)
plt.plot(sol.t,sol.y[0],'r-o',t,y2,'g')
plt.xlabel('t')
plt.ylabel('y')
plt.show()

# ODE3
def f3(t,y):
      return (1+y/t)
   #exact solution is
def exact3(t):
      return (t*(2+np.log(t)))


t=np.linspace(1,2)
sol=solve_ivp(f3,[1,2],[2],t_eval=np.linspace(1,2))

y3=exact3(t)
plt.plot(sol.t,sol.y[0],'r-o',t,y3,'g')
plt.xlabel('t')
plt.ylabel('y')
plt.show()
# ODE4
def f4(t,y):
      return (np.cos(2*t)+np.sin(3*t))

   #exact solution is
def exact4(t):
      return (np.sin(2*t)/2-np.cos(3*t)/3+4/3)


t=np.linspace(0,1)
sol=solve_ivp(f4,[0,1],[1],t_eval=np.linspace(0,1))

y4=exact4(t)
plt.plot(sol.t,sol.y[0],'r-o',t,y4,'g')
plt.xlabel('t')
plt.ylabel('y')
plt.show()



