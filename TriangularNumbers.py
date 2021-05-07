# Beta Round 44, Div 2, Problem A
# https://codeforces.com/contest/47/problem/A

from math import sqrt, floor
inp = int(input())
n = (sqrt(4*2*inp+1) - 1)/2
if floor(n) == n:
    print('YES')
else:
    print('NO')