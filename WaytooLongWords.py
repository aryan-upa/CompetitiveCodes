# Beta Round 65, Div 2, Problem A
# https://codeforces.com/contest/71/problem/A

n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in a:
    if len(i) > 10:
        L = len(i)
        change = f'{i[0]}{L - 2}{i[L - 1]}'
        print(change)
    else:
        print(i)