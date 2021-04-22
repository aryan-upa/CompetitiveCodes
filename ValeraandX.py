# Round 237, Div 2, Problem A
# http://codeforces.com/contest/404/problem/A

inp = int(input())
rem, mem = [], []
for i in range(inp):
    st = input()
    for q in range(inp):
        if q == inp-i-1 or q == i:
            mem.append(st[q])
        else:
            rem.append(st[q])
else:
    c = rem[0]
    m = mem[0]
    if c != m:
        if mem.count(m) != inp*2-1 or rem.count(c) != (inp**2 - inp*2+1):
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
