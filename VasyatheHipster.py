# Round 322, Div 2, Problem A
# https://codeforces.com/contest/581/problem/A

from math import fabs
a, b = map(int, input().split())
print(min(a,b), int(fabs(a-b)//2))