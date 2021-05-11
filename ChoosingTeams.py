# Round 246, Div 2, Problem A
# https://codeforces.com/contest/432/problem/A

n,k = map(int,input().split())
ls = list(map(int,input().split()))
ele = [q for q in ls if q<(6-k)]
print(len(ele)//3)
