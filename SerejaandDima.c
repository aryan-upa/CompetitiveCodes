// Round 233, Div 2, Problem A
// https://codeforces.com/contest/381/problem/A


#include<stdio.h>
 
int max(int a, int b)
{
    int Max;
    if(a>b)
    	Max=a;
   	else
   		Max=b;
    return Max;
}
 
int main()
{	
	int n;
	scanf("%d",&n);
	
	int i,j,arr[n];
	for(i=0;i<n;i++)
	{
	    scanf("%d",&arr[i]);
	}
    
    int k=0;
    i=0;j=n-1;
    int ser=0,dim=0;
    for(k=0;k<n;k++)
    {
   		if(k==1)
   		{
   			if(arr[i]>arr[j])
   			{
			   	dim+=arr[i];
			   	i++;
	   		}
	   		else
   			{
			   	dim+=arr[j];
			   	j--;
		    }   				
   		}
   		else if(k%2==0)
   		{
		   		if(arr[i]>arr[j])
   			{
			   	ser+=arr[i];
			   	i++;
	   		}
	   		else
   			{
			   	ser+=arr[j];
			   	j--;
		    }   					
	    }
	    else
	    {
   			if(arr[i]>arr[j])
   			{
			   	dim+=arr[i];
			   	i++;
	   		}
	   		else
   			{
			   	dim+=arr[j];
			   	j--;
		    }   				
   		
    	}
    }
    
    printf("%d %d\n",ser,dim);
}