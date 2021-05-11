# Beta Round 16, Div 2, Problem A
# https://codeforces.com/contest/16/problem/A

n,m = map(int,input().split())
ls = []
s = input()
if s != f'{s[0]}'*m:
    print('NO')
else:
    ls.append(s[0])
    for i in range(n-1):
        s = input()
        if ls.pop() == s[0]:
            print('NO')
            break
        elif s != f'{s[0]}'*m:
            print('NO')
            break
        ls.append(s[0])
    else:
        print('YES')
