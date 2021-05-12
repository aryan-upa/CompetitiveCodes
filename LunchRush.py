# Round 169, Div 2, Problem A
# https://www.codeforces.com/contest/276/problem/A

n,k = map(int,input().split())
joy = []
for q in range(n):
    f,t = map(int,input().split())
    if t>k:
        joy.append(f-(t-k))
    else:
        joy.append(f)
else:
    print(max(joy))