# Round 131, Div 2, Problem A
# https://codeforces.com/contest/214/problem/A

n,m = map(int,input().split()); _=0
for a in range(0,n+1):
    if int(a**4 - (2*(a**2))*n + a)==int(m - n*n):
        if n - a*a >=0:
            _+=1
else:
    print(_)