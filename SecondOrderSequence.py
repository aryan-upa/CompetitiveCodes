# Beta Round 22, Div 2, Problem A
# https://codeforces.com/contest/22/problem/A

inp = int(input())
ls = list(map(int, input().split()))
ls.sort()
m = ls[0]
for i in ls:
    if i!=m:
        print(i)
        break
else:
    print('NO')
