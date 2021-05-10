# Round 307, Div 2, Problem A
# https://codeforces.com/contest/551/problem/A

inp = input()
ls = list(map(int,input().split()))
ans = ls.copy()
ans.sort()
for i in ls:
    c = ls.count(i)
    pos = len(ans[ans.index(i):]) - (c-1)
    print(pos,end=' ')