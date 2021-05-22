# Beta Round 76, Div 2, Problem A
# http://codeforces.com/contest/94/problem/A

st = input()
ls = []
for i in range(10):
    ls.append(input())
pas = ''
for i in range(0,80,10):
    q = ls.index(st[i:i+10])
    pas+=str(q)
print(pas)
