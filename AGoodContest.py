# Round 357, Div 2, Problem A
# https://codeforces.com/contest/681/problem/A

inp= int(input())
for q in range(inp):
    n, b, a = map(str,input().split())
    b, a = int(b), int(a)
    if b>=2400:
        if a-b>0:
            print('YES')
            break
else:
    print('NO')