// Beta Round 85, Div 2, Problem A
// https://codeforces.com/contest/112/problem/A


#include <stdio.h>
#include <string.h>
 
int main ()
{
    char s1[100];
    char s2[100];
 
    gets(s1);
    gets(s2);
    
    
    int len=strlen (s1);
    int i;
    for(i=0;i<len;i++)
    {
        s1[i]=tolower(s1[i]);
        s2[i]=tolower(s2[i]);
    }
    
    int flag=0;
    int sum1=0,sum2=0;
    for(i=0;i<len;i++)
    {
        if(s1[i]!=s2[i])
        {
            flag=1;
            if((int)s1[i]>(int)s2[i])
                printf("1");
            else
                printf("-1");
            break;
        }
        else;
    }
    
    if(flag==0)
        printf("0");
    
    
    return 0;
}