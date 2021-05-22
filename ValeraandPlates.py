# Round 216, Div 2, Problem A
# http://codeforces.com/contest/369/problem/A

n,m,k = map(int,input().split())
a = list(map(int,input().split()))
wsh = 0
for i in a:
    if i==1:
        m-=1
        if m<0: wsh+=1
    else:
        if k>0: k-=1
        elif m>0: m-=1
        else: wsh+=1
print(wsh)