# Round 235, Div 2, Problem A
# https://codeforces.com/contest/401/problem/A

n,x = map(int,input().split())
ls = list(map(int, input().split()))
P = sum(ls); _=1
if P!=0:
    if P<0: P=-1*P
    while P>x:
        P-=x
        _+=1
    print(_)
else:
    print(0)
