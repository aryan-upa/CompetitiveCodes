# Round FF, Div 2, Problem A
# https://codeforces.com/contest/447/problem/A

p,n = map(int,input().split())
ls = [int(input()) for i in range(n)]
ls = [i % p for i in ls]
for q in range(n):
    if ls[q] in ls[:q]:
        print(q+1)
        break
else:
    print(-1)
