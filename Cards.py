# Round 364, Div 2, Problem A
# https://codeforces.com/contest/701/problem/A

inp = int(input())
ls = list(map(int, input().split()))
ans=[]
nls = ls.copy()
nls.sort()
for i in range(int(inp/2)):
    ele1,ele2 = nls[i],nls[inp-i-1]
    pos1 = ls.index(ele1)+1
    ls[ls.index(ele1)]=0
    pos2 = ls.index(ele2)+1
    ls[ls.index(ele2)]=0
    ans.append([pos1,pos2])
for i in ans:
    print(*i)