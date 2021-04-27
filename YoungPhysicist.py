# Beta Round 63, Div 2, Problem A
# https://codeforces.com/contest/69/problem/A

inp = int(input())
ls = [0, 0, 0]
for i in range(inp):
    q = list(map(int, input().split()))
    ls = [ls[i] + q[i] for i in range(3)]
else:
    print('YES') if ls.count(0)==3 else print('NO')