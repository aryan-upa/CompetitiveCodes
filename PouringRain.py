# Round 349, Div 2, Problem A
# https://codeforces.com/contest/667/problem/A

from math import pi
d,h,v,e = map(int,input().split())
Vol = pi*(d/2)**2*h
e = pi*(d/2)**2*e
if v-e<=0:
    print('NO')
else:
    print('YES')
    print(Vol/(v-e))
