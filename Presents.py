# Beta Round 97, Div 2, Problem A
# https://codeforces.com/contest/136/problem/A

inp = int(input())
ls = list(map(int, input().split()))
for i in range(1, inp+1):
    print(ls.index(i)+1, end=' ')