// Round 163, Div 2, Problem A
// https://codeforces.com/contest/266/problem/A

#include <stdio.h>
#include <string.h>
 
int main()
{
    long long int n;
    scanf("%lld",&n);
    char A[n];
    scanf("%s",&A);
    
    long long int i,count=0;
    char check = A[0];
    for(i=0;i<n-1;i++)
    {
        if(check==A[i+1])
        {
            count++;
        }
        else
            check=A[i+1];
    }
    
    printf("%lld",count);
    return 0;
}