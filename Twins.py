# Round 111, Div 2, Problem A
# https://codeforces.com/contest/160/problem/A

from math import ceil
inp = int(input())
ls = list(map(int, input().split()))
ls.sort(reverse=True)
Mx = sum(ls)
if Mx % 2 == 0:
    Mx = Mx/2 + 1
else:
    Mx = ceil(Mx/2)
sm, count = 0, 0
for i in ls:
    if sm >= Mx:
        break
    else:
        sm += i
        count += 1
print(count)