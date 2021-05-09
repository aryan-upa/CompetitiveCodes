# Round 301, Div 2, Problem A
# https://codeforces.com/contest/540/problem/A

from math import fabs
inp = int(input()); pos = input()
req,sm = input(),0
for i in range(inp):
    _ = fabs(int(pos[i])-int(req[i]))
    sm= (sm +10-_) if (_>5) else (sm + _)
print(int(sm))