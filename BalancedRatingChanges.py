# Global Round 5, Problem A
# https://codeforces.com/contest/1237/problem/A

from math import ceil,floor
inp = int(input()); ls = [int(input()) for a in range(inp)]
flag=0
for i in range(len(ls)):
    if ls[i]%2!=0:
        if flag==0:
            ls[i] = ceil(ls[i]/2)
            flag+=1
        else:
            ls[i] = floor(ls[i]/2)
            flag-=1
    else:
        ls[i] = int(ls[i]/2)
print(*ls, sep='\n')