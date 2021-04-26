# Round 224, Div 2, Problem A
# https://codeforces.com/contest/382/problem/A

from math import fabs
ls, ly = map(str, input().split('|'))
inp = input()
if len(inp) < fabs(len(ls)-len(ly)):
    print('Impossible')
elif (len(inp) - fabs(len(ls)-len(ly)) )% 2 != 0:
    print('Impossible')
else:
    ls = list(ls)
    ly = list(ly)
    inp = list(inp)
    for i in inp:
        if len(ls) > len(ly):
            ly.append(i)
        else:
            ls.append(i)
    out = ls
    out.append('|')
    out += ly
    print(*out, sep='')