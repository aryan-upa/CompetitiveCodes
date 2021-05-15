# Round 363, Div 2, Problem A
# https://codeforces.com/contest/699/problem/A

inp = int(input())
st = input()
ls = list(map(int, input().split()))
pos = []
for q in range(inp-1):
    if st[q]=='R':
        if st[q+1]=='L':
            pos.append(q)
if len(pos) == 0:
    print(-1)
else:
    _ = []
    for j in pos:
        dif = ls[j+1] - ls[j]
        _.append(dif/2)
    print(int(min(_)))