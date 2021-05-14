# Beta Round 59, Div 2, Problem A
# https://codeforces.com/contest/63/problem/A

n = int(input())
na = []; ra = []
for i in range(n):
    a,b = map(str,input().split())
    na.append(a); ra.append(b)
for q in range(len(ra)):
    if ra[q] == 'rat':
        print(na[q])
for q in range(len(ra)):
    if ra[q] == 'child' or ra[q] == 'woman':
        print(na[q])
for q in range(len(ra)):
    if ra[q] == 'man':
        print(na[q])
for q in range(len(ra)):
    if ra[q] == 'captain':
        print(na[q])