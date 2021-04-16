// Round 200, Div 2, Problem A
// https://codeforces.com/contest/344/problem/A


#include <stdio.h>
 
int main()
{
    long long int n;
    scanf("%lld",&n);
    
    long long int i,A[n];
    for(i=0;i<n;i++)
    {
        scanf("%lld",&A[i]);
    }
    
    long long int count=0;
    for(i=0;i<n-1;i++)
    {
        if(A[i]==A[i+1]);
        else
            count++;
    }
    
    printf("%lld\n",count+1);
}