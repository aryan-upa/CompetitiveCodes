// Round 238, Div 2, Problem A
// https://codeforces.com/contest/405/problem/A

#include<stdio.h>
 
int main()
{
	long long int a;
	scanf("%lld",&a);
	
	long long int A[a];
	long long int i;
	for(i=0;i<a;i++)
	{
		scanf("%lld",&A[i]);
	}
	
	long long int j;
	for(i=0;i<a;i++)
	{
		for(j=0;j<a;j++)
		{
			if(A[j]>A[j+1])
			{
				long long int temp=A[j];
				A[j]=A[j+1];
				A[j+1]=temp;
			}
			else
				continue;
		}
	}
	
	for(i=0;i<a;i++)
		printf("%lld ",A[i]);
 
    return 0;
}