#include<stdio.h>
#include<math.h>

float fun(float t,float y)
{
    float f, t2;
    t2=pow(t, 2);
    f=y-t2+1;
    return f;
}

float g(float t)
{
	float T, yexact;
	T=pow((t+1), 2);
	yexact=T-0.5*exp(t);
	return yexact;
}

float errbd(float t)
{
	float errbound;
	errbound=0.1*(0.5*exp(2)-2)*(exp(t)-1);
	return errbound;
}
			
int main()
{
    int i;
	float a=0,b=2,h=0.1;
	int N=(b-a)/h;		//No. of steps
	float y[N+1];
	float t[N+1];
	float y_exact[N+1];
	float error[N+1];
	float err_bound[N+1];
	
	for(i=0;i<N+1;i++)
	{
		y[i]=0;		
		t[i]=a+i*h;	//Mesh points
	}
	
	y[0]=0.5;		//Initial condition
	for(i=0;i<N+1;i++)
	{
		y[i+1]=y[i]+h*fun(t[i],y[i]);		//Euler's method
		y_exact[i]=g(t[i]);	//exact solution
		error[i]=y_exact[i]-y[i];	   //Absolute error
		err_bound[i]=errbd(t[i]); //Error bound with using  Lipschitz criterion
	}
	printf("No of          y_exact      Error           Error \n");
	printf("iteration                                  bound\n");  // initiation of table
	for(i=0;i<10;i++)
	{
		printf("%d         %f         %f             %f\n" ,i,y_exact[i],error[i], err_bound[i]);
	}
	for(i=10;i<N+1;i++)
	{
		printf("%d        %f          %f               %f\n" ,i,y_exact[i],error[i], err_bound[i]);
	}
	  
       
       
    return 0;
}
