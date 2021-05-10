# Round 170, Div 2, Problem A
# https://codeforces.com/contest/278/problem/A

inp = int(input())
ls = list(map(int, input().split()))
s1,s2 = map(int,input().split())
if s1>s2: s1,s2 = s2,s1
print(min(sum(ls[s1-1:s2-1]),sum(ls[:s1-1])+sum(ls[s2-1:])))