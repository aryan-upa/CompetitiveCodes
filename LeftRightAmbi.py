# Round 469, Div 2, Problem A
# http://codeforces.com/contest/950/problem/A

from math import fabs
l, r, a = map(int,input().split())
if fabs(l-r)<a:
    c = (l+r+a) if (l+r+a)%2==0 else l+r+a-1
elif fabs(l-r)>a:
    c = 2*(min(l,r) + a)
else:
    c = l+r+a
print(c)