# Round 167, Div 2, Problem A
# https://codeforces.com/contest/272/problem/A

n = int(input())
ls = list(map(int,input().split()))
S = sum(ls)
val = 5
for i in range(1,6):
    if (S+i) % (n+1)==1:
        val-=1
else:
    print(val)
