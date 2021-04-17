# VK Cup 2017, Qualification 2, Problem A
# https://codeforces.com/contest/770/problem/A

from itertools import cycle
st = 'abcdefghijklmnopqrstuvwxyz'
ls = list(map(int, input().split()))
l, k = ls[0], ls[1]
os = ''
ls = list(st[0:k])
pool = cycle(ls)
while len(os) < l:
    os += next(pool)
print(os)
