# Round 150, Div 2, Problem A
# https://codeforces.com/contest/244/problem/A

n,k = map(int,input().split())
ls = list(map(int,input().split()))
ps = [q for q in range(1,n*k+1) if q not in ls]
ps = iter(ps)
for i in range(k):
    print(ls[i],end=' ')
    for q in range(n-1):
        print(next(ps),end=' ')
    print()