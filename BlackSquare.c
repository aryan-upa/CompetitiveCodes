// Round 247, Div 2, Problem A
// https://codeforces.com/contest/431/problem/A


#include<stdio.h>
#include<string.h>
 
int main()
{
    
    long long int a,b,c,d;
    scanf("%lld %lld %lld %lld",&a,&b,&c,&d);
    
    char str[100000];
    scanf("%s",&str);
    long long int len=strlen(str);
    long long int i;
    long long int sum=0;
    for(i=0;i<len;i++)
    {
        int val= str[i];
        switch(val)
        {
            case(49): sum+= a;
                break;
            case(50): sum+= b;
                break;
            case(51): sum+= c;
                break;
            case(52): sum+= d;
                break;
        };
    }
    
    printf("%lld",sum);
    return 0;
}