# Beta Round 42, Div 2, Problem A
# https://codeforces.com/contest/43/problem/A

inp = int(input())
if inp == 1:
    print(input())
else:
    ls = []
    for i in range(inp):
        P = input()
        ls.append(P)
    t1, t2 = 0, 0
    T1 = ls[0]
    T2 = ''
    for i in ls:
        if i == ls[0]:
            t1 += 1
        else:
            T2 = i
            t2 += 1
    if t1>t2:
        print(T1)
    else:
        print(T2)