# Beta Round 93, Div 2, Problem A
# http://codeforces.com/contest/127/problem/A

from math import sqrt
def Sep(a,b):
    return sqrt(a**2 + b**2)
n, k = map(int, input().split())
x1, y1 = map(int, input().split())
dist = 0
for i in range(n-1):
    x2, y2 = map(int, input().split())
    dist+= Sep(x2-x1,y2-y1)
    x1, y1 = x2, y2
print(dist*k/50)