// Round 178, Div 2, Problem A
// https://codeforces.com/contest/294/problem/A


#include <stdio.h>
 
int main() 
{
	int n;
	scanf("%d",&n);
	int i,Arr[n];
	for(i=0;i<n;i++)
	    scanf("%d",&Arr[i]);
	    
	int m;
	scanf("%d",&m);
	int X[m],Y[m];
	for(i=0;i<m;i++)
	    scanf("%d %d",&X[i],&Y[i]);
	
	for(i=0;i<m;i++)
	{
	    int val=X[i]-1;
	    int shot=Y[i];
	    if(val!=0||val!=n-1)
	    {
	        Arr[val-1]+=shot-1;
	        Arr[val+1]+=Arr[val]-shot;
	        Arr[val]=0;
	    }
	    else if(i==0)
	    {
	        Arr[val+1]+=Arr[val]-shot;
	        Arr[val]=0;
	    }
	    else
	    {
	        Arr[val-1]+=shot-1;
	        Arr[val]=0;
	    }
	}
	
	for(i=0;i<n;i++)
	    printf("%d\n",Arr[i]);
	
	return 0;
}