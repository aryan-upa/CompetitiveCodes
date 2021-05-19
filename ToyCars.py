# Round 303, Div 2, Problem A
# https://codeforces.com/contest/545/problem/A

inp = int(input())
ls = [list(map(int,input().split())) for q in range(inp)]
crs = [0 for j in range(inp)]
for i in range(inp):
    p = ls[i]; val=0
    for j in p:
        if j==1:
            crs[i]=-1
        elif j==2:
            crs[val]=-1
        elif j==3:
            crs[i]=-1
            crs[val]=-1
        val += 1
if crs.count(0)==0:
    print(0)
else:
    print(crs.count(0))
    for i in range(inp):
        if crs[i]!=-1:
            print(i+1,end=' ')
