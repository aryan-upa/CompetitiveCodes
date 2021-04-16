// Round 164, Div 2, Problem A
// https://codeforces.com/contest/268/problem/A


#include <stdio.h>
#include <string.h>
 
int main()
{
    int n;
    scanf("%d",&n);
    int i;
    int A[n],B[n];
    for(i=0;i<n;i++)
    {scanf("%d %d",&A[i],&B[i]);}
    
    int count=0;
    for(i=0;i<n;i++)
    {
        int j;
        for(j=0;j<n;j++)
        {
            if(A[i]==B[j])
                count++;
            else;
        }
    }
    
    printf("%d",count);
    return 0;
}