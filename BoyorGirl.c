// Round 146, Div 2, Problem A
// https://codeforces.com/contest/236/problem/A


#include<stdio.h>
#include<string.h>

int main()
{
	char s[100];
	gets(s);
	
	int len = strlen(s);
	int i;
	int count=0;
	for(i=0;i<len;i++)
	{
		int j,flag=0;
		for(j=0;j<i;j++)
		{
			if(s[i]==s[j])
			{
				flag=1;
				break;
			}
			else
				continue;
		}
		if(flag==0)
		    count++;
		else;
	}
	
	if(count==1)
	    printf("IGNORE HIM!\n");
	else if(count%2==0)
	    printf("CHAT WITH HER!\n");
	else
	    printf("IGNORE HIM!\n");
}