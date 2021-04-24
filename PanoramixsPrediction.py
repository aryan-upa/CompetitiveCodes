# Beta Round 69, Div 2, Problem A
# https://codeforces.com/contest/80/problem/A

m, n = map(int, input().split())
ls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if ls.index(m) != 14:
    if n == ls[ls.index(m)+1]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')