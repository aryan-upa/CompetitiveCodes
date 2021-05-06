# Round 222, Div 2, Problem A
# https://codeforces.com/contest/378/problem/A

from math import ceil
c1, c2 = map(int, input().split())
low, high = min(c1,c2), max(c1,c2)

if (high-low)%2==0:
    t = int((high+low)/2)
    chigh = 6 - t
    clow = t - 1
    if high == c1:
        print(chigh,1,clow)
    else:
        print(clow,1,chigh)
else:
    t = (high + low)/2
    chigh = ceil(6 - t)
    clow = ceil(t - 1)
    if high == c1:
        print(chigh,0,clow)
    else:
        print(clow,0,chigh)
