# Round 177, Div 2, Problem A
# https://codeforces.com/contest/289/problem/A

n,k = map(int, input().split())
val = 0
for i in range(n):
    l,r = map(int,input().split())
    val+=r-l+1
if val%k!=0:
    print(k-val%k)
else:
    print(0)