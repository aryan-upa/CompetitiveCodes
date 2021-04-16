// Round 244, Div 2, Problem A
// https://codeforces.com/contest/427/problem/A

#include<stdio.h>
 
int main()
{
    long long int n;
    scanf("%lld",&n);
    
    long long int i,A[n];
    long long int C=0,P=0,count=0;
    for(i=0;i<n;i++)
    {
        scanf("%lld",&A[i]);
        if(A[i]==-1)
        {
            if(P>0)
                P-=1;
            else
                count++;
        }
        else
        {
            P+=A[i];
        }
    }
    
    printf("%lld",count);
    return 0;
}