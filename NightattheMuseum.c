// Round 376, Div 2, Problem A
// https://codeforces.com/contest/731/problem/A


#include <stdio.h>
#include <string.h>
 
int work(int x, int y)
{
    if(x>y)
    {int k=x;x=y;y=k;}
    
    int p= y-x;
    int P=x+26-y;
    if(P<p)
        return P;
    else
        return p;
}
 
int main()
{
    char str[100];
    scanf("%s",&str);
    
    int i,len=strlen(str);
    int sum=0;
    char point='a';
    for(i=0;i<len;i++)
    {
        sum+=work(point,str[i]);
        point=str[i];
    }
    
    printf("%d",sum);
    return 0;
}