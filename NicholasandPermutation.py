# Round 354, Div 2, Problem A
# https://codeforces.com/contest/676/problem/A

n = int(input())
ls = list(map(int,input().split()))
pos1 = ls.index(min(ls))
pos2 = ls.index(max(ls))
if pos2<pos1:
    pos2,pos1=pos1,pos2
print(max(n-1-pos1,pos2))