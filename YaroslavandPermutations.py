# Round 179, Div 2, Problem A
# https://codeforces.com/contest/296/problem/A

from math import ceil
inp = int(input())
ls = list(map(int, input().split()))
dist = [ls[0]]
for i in ls:
    if i not in dist:
        dist.append(i)
dist = [ls.count(q) for q in dist]
if max(dist) >= ceil(inp/2) + 1:
    print('NO')
else:
    print('YES')