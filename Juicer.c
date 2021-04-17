// AIM Tech Round 3, Div 2, Problem A
// https://codeforces.com/contest/709/problem/A

#include <stdio.h>
 
int main(void) 
{
	unsigned long int n,b,d;
	scanf("%u %u %u",&n,&b,&d);
	
	unsigned long int i,Arr[n],count=0;
	for(i=0;i<n;i++)
	{
	    unsigned long int val;
	    scanf("%u",&val);
	    if(val>b);
	    else
	    {
	        Arr[count]=val;
	        count++;
	    }
	}
	
	unsigned long int rem=0,sum=0;
	unsigned int T=0;
	i=0;
	while(i<count)
	{
	   sum+=Arr[i]+rem;
	   if(sum>d)
	   {
	       T++;
	       rem=0;
	       sum=0;
	   }
	   else
	   {
	       rem=0;
	   }
	   i++; 
	}
	
	printf("%u",T);
	
	return 0;
}