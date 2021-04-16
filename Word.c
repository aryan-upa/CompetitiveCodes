// Beta Round 55, Div 2, Problem A
// https://codeforces.com/contest/59/problem/A

#include <stdio.h>
#include <string.h>
#include <ctype.h>
 
int main()
{
    char s[100];
    gets(s);
    
    int i,len= strlen(s);
    int up=0,lo=0;
    for(i=0;i<len;i++)
    {
        if(isupper(s[i]))
            up++;
        else
            lo++;
    }
    
    if(up>lo)
    {
        for(i=0;i<len;i++)
            s[i]=toupper(s[i]);
    }
    else
    {
        for(i=0;i<len;i++)
            s[i]=tolower(s[i]);
    }
    
    puts(s);
}