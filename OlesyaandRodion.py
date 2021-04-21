# Round 394, Div 2, Problem A
# https://codeforces.com/contest/584/problem/A

n, t = map(int, input().split())
if n == 1:
    if t >= 10:
        print(-1)
    else:
        print(t)
elif t == 10:
    print(10**(n-1))
else:
    c = str(t)
    print(c*n)