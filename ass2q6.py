import numpy as np
import matplotlib.pyplot as plt

a=0
b=10
h=0.1
n=int((b-a)/h)
#construction of A,B matrix for solving the equation Ax=b
A=np.zeros((n,n))
A[0,0]=-2
A[0,1]=1
A[n-1,n-1]=-2
A[n-1,n-2]=1
for i in range(1,n-1):
    A[i,i]=-2
    A[i,i+1]=1
    A[i,i-1]=1
t=np.linspace(a,b,n+1)
B=-10*h**2*np.ones(n)
y=np.linalg.solve(A,B)
x=np.zeros(n)
w=1.75
count=0
for l in range(n):
    while(abs(x[l]-y[l])>=0.00001):
        for j in range(n):
            p=B[j]
            for k in range(n):
                if(k!=j):
                    p=p-A[j][k]*x[k]
                
                v=p/A[k][k]
            x[j]=w*v+(1-w)*x[j]
    
        
        count=count+1
        if count%100==0:
            plt.plot(t,np.append(x,0),'--',color="black")

print('Iteration=',count)            

plt.plot(t,np.append(x,0),'g-o',label="Using relaxation method")
plt.plot(t,np.append(y,0),color="red",label="Exact solution")    
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.show()


