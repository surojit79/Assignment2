import matplotlib.pyplot as plt
import numpy as np
def f(x,y):
    return ((y/x)-(y/x)**2)
a=1 
b=2 
h= 0.1 
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
y = np.zeros((n+1,))
x[0]=1
y[0]=1
yt=(x/(1+np.log(x)))
for j in range(1,n+1):
    y[j] = y[j-1] + h*f(x[j-1],y[j-1])
Abserror=sum(yt-y)
print('Abserror =',Abserror)
Relerror=sum((yt-y)/yt)
print('Relerror = ',Relerror)
plt.xlabel('x')
plt.ylabel('y')
plt.title( "Forward Euler’s Method with, h= 0.1" )
plt.plot(x,y,color ='r',label = 'Euler Method')
plt.plot(x,yt,color = 'g',label = 'Analytcal Solution')
plt.legend()
plt.grid()
plt.show()
