# Round 267, Div 2, Problem A
# http://codeforces.com/contest/467/problem/A

inp, _ = int(input()), 0
for i in range(inp):
    q, p = map(int, input().split())
    if p-q>=2:
        _+=1
print(_)