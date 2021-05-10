# Round 225, Div 2, Problem A
# https://codeforces.com/contest/384/problem/A

from math import ceil
inp = int(input())
print(ceil(inp*inp/2))
for i in range(inp):
    st=''
    if i%2==0:
        for q in range(inp):
            st+='C' if q%2==0 else '.'
    else:
        for q in range(inp):
            st+='.' if q%2==0 else 'C'
    print(st)