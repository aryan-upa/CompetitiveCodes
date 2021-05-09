# Round 107, Div 2, Problem A
# https://codeforces.com/contest/151/problem/A

from math import floor
n, k, l, c, d, p, nl, np = map(int,input().split())
print(min(floor((k*l)/(n*nl)),floor((c*d)/(n)),floor(p/(n*np))))